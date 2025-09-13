from flask import Blueprint, request, jsonify
from src.models.customer import db, Customer, ServiceRecord, Appointment
from datetime import datetime, date, timedelta
import csv
import os

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    """Get all customers"""
    try:
        customers = Customer.query.all()
        return jsonify([customer.to_dict() for customer in customers])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get a specific customer"""
    try:
        customer = Customer.query.get_or_404(customer_id)
        return jsonify(customer.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    """Create a new customer"""
    try:
        data = request.get_json()
        
        customer = Customer(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone=data.get('phone'),
            email=data.get('email'),
            address=data.get('address'),
            city=data.get('city'),
            state=data.get('state'),
            zip_code=data.get('zip_code'),
            property_type=data.get('property_type'),
            hvac_system_type=data.get('hvac_system_type'),
            hvac_system_age=data.get('hvac_system_age'),
            preferred_contact_method=data.get('preferred_contact_method'),
            notes=data.get('notes')
        )
        
        db.session.add(customer)
        db.session.commit()
        
        return jsonify(customer.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update a customer"""
    try:
        customer = Customer.query.get_or_404(customer_id)
        data = request.get_json()
        
        for key, value in data.items():
            if hasattr(customer, key):
                setattr(customer, key, value)
        
        customer.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify(customer.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>/service-records', methods=['GET'])
def get_customer_service_records(customer_id):
    """Get service records for a customer"""
    try:
        records = ServiceRecord.query.filter_by(customer_id=customer_id).all()
        return jsonify([record.to_dict() for record in records])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/service-records', methods=['POST'])
def create_service_record():
    """Create a new service record"""
    try:
        data = request.get_json()
        
        # Parse date string to date object
        service_date = datetime.strptime(data.get('service_date'), '%Y-%m-%d').date()
        
        record = ServiceRecord(
            customer_id=data.get('customer_id'),
            service_date=service_date,
            service_type=data.get('service_type'),
            duration_hours=data.get('duration_hours'),
            technician=data.get('technician'),
            services_performed=data.get('services_performed'),
            findings=data.get('findings'),
            recommendations=data.get('recommendations'),
            parts_used=data.get('parts_used'),
            labor_cost=data.get('labor_cost'),
            parts_cost=data.get('parts_cost'),
            total_cost=data.get('total_cost'),
            payment_method=data.get('payment_method'),
            payment_status=data.get('payment_status'),
            customer_satisfaction=data.get('customer_satisfaction'),
            follow_up_required=data.get('follow_up_required', False),
            notes=data.get('notes')
        )
        
        db.session.add(record)
        
        # Update customer's total services count
        customer = Customer.query.get(data.get('customer_id'))
        if customer:
            customer.total_services += 1
            customer.last_service_date = service_date
        
        db.session.commit()
        
        return jsonify(record.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/appointments', methods=['GET'])
def get_appointments():
    """Get all appointments"""
    try:
        appointments = Appointment.query.all()
        result = []
        for appointment in appointments:
            appointment_dict = appointment.to_dict()
            # Add customer name for display
            customer = Customer.query.get(appointment.customer_id)
            if customer:
                appointment_dict['customer_name'] = f"{customer.first_name} {customer.last_name}"
                appointment_dict['customer_phone'] = customer.phone
                appointment_dict['customer_address'] = f"{customer.address}, {customer.city}, {customer.state} {customer.zip_code}"
            result.append(appointment_dict)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/appointments', methods=['POST'])
def create_appointment():
    """Create a new appointment"""
    try:
        data = request.get_json()
        
        # Parse date and time strings
        scheduled_date = datetime.strptime(data.get('scheduled_date'), '%Y-%m-%d').date()
        scheduled_time = datetime.strptime(data.get('scheduled_time'), '%H:%M').time()
        
        appointment = Appointment(
            customer_id=data.get('customer_id'),
            service_type=data.get('service_type'),
            scheduled_date=scheduled_date,
            scheduled_time=scheduled_time,
            estimated_duration=data.get('estimated_duration'),
            status=data.get('status', 'Scheduled'),
            special_instructions=data.get('special_instructions'),
            confirmed=data.get('confirmed', False),
            notes=data.get('notes')
        )
        
        db.session.add(appointment)
        db.session.commit()
        
        return jsonify(appointment.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/import-sample-data', methods=['POST'])
def import_sample_data():
    """Import sample data from CSV files"""
    try:
        # Import customers
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'hvac_dr_customer_database.csv')
        if os.path.exists(csv_path):
            with open(csv_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Check if customer already exists
                    existing = Customer.query.filter_by(phone=row['Phone']).first()
                    if not existing:
                        customer = Customer(
                            first_name=row['First_Name'],
                            last_name=row['Last_Name'],
                            phone=row['Phone'],
                            email=row['Email'],
                            address=row['Address'],
                            city=row['City'],
                            state=row['State'],
                            zip_code=row['ZIP'],
                            property_type=row['Property_Type'],
                            hvac_system_type=row['HVAC_System_Type'],
                            hvac_system_age=row['HVAC_System_Age'],
                            last_service_date=datetime.strptime(row['Last_Service_Date'], '%Y-%m-%d').date() if row['Last_Service_Date'] else None,
                            next_service_due=datetime.strptime(row['Next_Service_Due'], '%Y-%m-%d').date() if row['Next_Service_Due'] else None,
                            preferred_contact_method=row['Preferred_Contact_Method'],
                            notes=row['Notes'],
                            customer_since=datetime.strptime(row['Customer_Since'], '%Y-%m-%d').date() if row['Customer_Since'] else None,
                            total_services=int(row['Total_Services']) if row['Total_Services'] else 0,
                            customer_rating=int(row['Customer_Rating']) if row['Customer_Rating'] else 5
                        )
                        db.session.add(customer)
        
        db.session.commit()
        return jsonify({'message': 'Sample data imported successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/dashboard-stats', methods=['GET'])
def get_dashboard_stats():
    """Get dashboard statistics"""
    try:
        total_customers = Customer.query.count()
        total_appointments = Appointment.query.count()
        pending_appointments = Appointment.query.filter_by(status='Scheduled').count()
        total_services = ServiceRecord.query.count()
        
        # Recent customers (last 30 days)
        thirty_days_ago = datetime.utcnow().date() - timedelta(days=30)
        recent_customers = Customer.query.filter(Customer.created_at >= thirty_days_ago).count()
        
        return jsonify({
            'total_customers': total_customers,
            'total_appointments': total_appointments,
            'pending_appointments': pending_appointments,
            'total_services': total_services,
            'recent_customers': recent_customers
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


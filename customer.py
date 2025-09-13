from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    property_type = db.Column(db.String(50))
    hvac_system_type = db.Column(db.String(100))
    hvac_system_age = db.Column(db.String(20))
    last_service_date = db.Column(db.Date)
    next_service_due = db.Column(db.Date)
    preferred_contact_method = db.Column(db.String(20))
    notes = db.Column(db.Text)
    customer_since = db.Column(db.Date, default=datetime.utcnow)
    total_services = db.Column(db.Integer, default=0)
    customer_rating = db.Column(db.Integer, default=5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with service records
    service_records = db.relationship('ServiceRecord', backref='customer', lazy=True)
    appointments = db.relationship('Appointment', backref='customer', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'property_type': self.property_type,
            'hvac_system_type': self.hvac_system_type,
            'hvac_system_age': self.hvac_system_age,
            'last_service_date': self.last_service_date.isoformat() if self.last_service_date else None,
            'next_service_due': self.next_service_due.isoformat() if self.next_service_due else None,
            'preferred_contact_method': self.preferred_contact_method,
            'notes': self.notes,
            'customer_since': self.customer_since.isoformat() if self.customer_since else None,
            'total_services': self.total_services,
            'customer_rating': self.customer_rating,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class ServiceRecord(db.Model):
    __tablename__ = 'service_records'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    service_date = db.Column(db.Date, nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    duration_hours = db.Column(db.Float)
    technician = db.Column(db.String(50))
    services_performed = db.Column(db.Text)
    findings = db.Column(db.Text)
    recommendations = db.Column(db.Text)
    parts_used = db.Column(db.String(200))
    labor_cost = db.Column(db.Numeric(10, 2))
    parts_cost = db.Column(db.Numeric(10, 2))
    total_cost = db.Column(db.Numeric(10, 2))
    payment_method = db.Column(db.String(20))
    payment_status = db.Column(db.String(20))
    customer_satisfaction = db.Column(db.Integer)
    follow_up_required = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'service_date': self.service_date.isoformat() if self.service_date else None,
            'service_type': self.service_type,
            'duration_hours': float(self.duration_hours) if self.duration_hours else None,
            'technician': self.technician,
            'services_performed': self.services_performed,
            'findings': self.findings,
            'recommendations': self.recommendations,
            'parts_used': self.parts_used,
            'labor_cost': float(self.labor_cost) if self.labor_cost else None,
            'parts_cost': float(self.parts_cost) if self.parts_cost else None,
            'total_cost': float(self.total_cost) if self.total_cost else None,
            'payment_method': self.payment_method,
            'payment_status': self.payment_status,
            'customer_satisfaction': self.customer_satisfaction,
            'follow_up_required': self.follow_up_required,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False)
    scheduled_time = db.Column(db.Time, nullable=False)
    estimated_duration = db.Column(db.Float)
    status = db.Column(db.String(20), default='Scheduled')
    special_instructions = db.Column(db.Text)
    confirmed = db.Column(db.Boolean, default=False)
    reminder_sent = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'service_type': self.service_type,
            'scheduled_date': self.scheduled_date.isoformat() if self.scheduled_date else None,
            'scheduled_time': self.scheduled_time.isoformat() if self.scheduled_time else None,
            'estimated_duration': float(self.estimated_duration) if self.estimated_duration else None,
            'status': self.status,
            'special_instructions': self.special_instructions,
            'confirmed': self.confirmed,
            'reminder_sent': self.reminder_sent,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


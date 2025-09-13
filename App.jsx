import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Phone, Mail, MapPin, Clock, CheckCircle, Wind, Thermometer, Shield, Star } from 'lucide-react'
import hvacLogo from './assets/hvac_dr_logo_hvac_only_1.png'
import './App.css'

function App() {
  const [activeService, setActiveService] = useState(0)

  const services = [
    {
      title: "Seasonal HVAC Tune-Up & Inspection",
      description: "Comprehensive system preparation for peak performance",
      features: [
        "Thorough system inspection",
        "Coil cleaning (condenser & evaporator)",
        "Blower component cleaning",
        "Lubrication of moving parts",
        "Air filter inspection & replacement",
        "Performance testing & detailed report"
      ],
      icon: <Thermometer className="w-8 h-8" />
    },
    {
      title: "HVAC Coil Deep Cleaning",
      description: "Restore efficiency and improve indoor air quality",
      features: [
        "Advanced coil cleaning techniques",
        "Indoor and outdoor coil treatment",
        "Condensate drain line clearing",
        "Coil integrity inspection",
        "Improved energy efficiency",
        "Better air circulation"
      ],
      icon: <Wind className="w-8 h-8" />
    },
    {
      title: "Basic System Check & Troubleshooting",
      description: "Quick diagnosis and resolution of common issues",
      features: [
        "Initial diagnostic assessment",
        "Basic troubleshooting procedures",
        "Minor adjustments and fixes",
        "Clear problem explanation",
        "Solution recommendations",
        "Professional referrals when needed"
      ],
      icon: <Shield className="w-8 h-8" />
    }
  ]

  const benefits = [
    { icon: <CheckCircle className="w-6 h-6 text-green-600" />, text: "Specialized Expertise" },
    { icon: <Clock className="w-6 h-6 text-blue-600" />, text: "Convenient Scheduling" },
    { icon: <Star className="w-6 h-6 text-yellow-600" />, text: "Transparent Pricing" },
    { icon: <Wind className="w-6 h-6 text-cyan-600" />, text: "Improved Air Quality" }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-3">
              <img src={hvacLogo} alt="HVAC Dr. Logo" className="h-12 w-12" />
              <div>
                <h1 className="text-2xl font-bold text-gray-900">HVAC Dr.</h1>
                <p className="text-sm text-gray-600">Expert HVAC Care</p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-6">
              <div className="flex items-center space-x-2 text-gray-600">
                <Phone className="w-4 h-4" />
                <span className="text-sm">[Your Phone Number]</span>
              </div>
              <Button className="bg-blue-600 hover:bg-blue-700">
                Get Free Quote
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center">
          <Badge className="mb-4 bg-blue-100 text-blue-800 hover:bg-blue-100">
            Serving Crittenden County, Arkansas
          </Badge>
          <h2 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
            Your Home's Breath of <span className="text-blue-600">Fresh Air</span>
          </h2>
          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Expert HVAC cleaning and servicing for a healthier, more efficient home. 
            We specialize in keeping your heating and cooling systems running smoothly, 
            efficiently, and cleanly.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-lg px-8 py-3">
              Schedule Service Today
            </Button>
            <Button size="lg" variant="outline" className="text-lg px-8 py-3">
              Learn More
            </Button>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h3 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Our Specialized Services
            </h3>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Focused expertise in HVAC cleaning and preventative maintenance 
              to keep your system running at peak performance.
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <Card 
                key={index}
                className={`cursor-pointer transition-all duration-300 hover:shadow-lg ${
                  activeService === index ? 'ring-2 ring-blue-500 shadow-lg' : ''
                }`}
                onClick={() => setActiveService(index)}
              >
                <CardHeader>
                  <div className="flex items-center space-x-3 mb-3">
                    <div className="p-2 bg-blue-100 rounded-lg text-blue-600">
                      {service.icon}
                    </div>
                  </div>
                  <CardTitle className="text-xl">{service.title}</CardTitle>
                  <CardDescription className="text-gray-600">
                    {service.description}
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2">
                    {service.features.map((feature, featureIndex) => (
                      <li key={featureIndex} className="flex items-start space-x-2">
                        <CheckCircle className="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" />
                        <span className="text-sm text-gray-700">{feature}</span>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Us Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h3 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Why Choose HVAC Dr.?
            </h3>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {benefits.map((benefit, index) => (
              <div key={index} className="text-center">
                <div className="flex justify-center mb-4">
                  <div className="p-3 bg-white rounded-full shadow-md">
                    {benefit.icon}
                  </div>
                </div>
                <h4 className="text-lg font-semibold text-gray-900 mb-2">
                  {benefit.text}
                </h4>
                <p className="text-gray-600 text-sm">
                  {benefit.text === "Specialized Expertise" && "Focused on cleaning and preventative maintenance for optimal system health."}
                  {benefit.text === "Convenient Scheduling" && "Weekend and evening appointments available to fit your busy schedule."}
                  {benefit.text === "Transparent Pricing" && "Clear, upfront quotes with no hidden fees or surprises."}
                  {benefit.text === "Improved Air Quality" && "Breathe easier with a cleaner, healthier HVAC system."}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-20 bg-blue-600 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h3 className="text-3xl md:text-4xl font-bold mb-4">
            Ready for a Healthier Home?
          </h3>
          <p className="text-xl mb-8 opacity-90">
            Contact HVAC Dr. today for expert HVAC cleaning and servicing.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-8 justify-center items-center mb-8">
            <div className="flex items-center space-x-2">
              <Phone className="w-5 h-5" />
              <span className="text-lg">[Your Phone Number Here]</span>
            </div>
            <div className="flex items-center space-x-2">
              <Mail className="w-5 h-5" />
              <span className="text-lg">[Your Email Here]</span>
            </div>
            <div className="flex items-center space-x-2">
              <MapPin className="w-5 h-5" />
              <span className="text-lg">Crittenden County, AR</span>
            </div>
          </div>

          <Button size="lg" className="bg-white text-blue-600 hover:bg-gray-100 text-lg px-8 py-3">
            Schedule Your Service Today
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center space-x-3 mb-4 md:mb-0">
              <img src={hvacLogo} alt="HVAC Dr. Logo" className="h-8 w-8 invert" />
              <div>
                <h4 className="text-lg font-bold">HVAC Dr.</h4>
                <p className="text-sm text-gray-400">Expert HVAC Care</p>
              </div>
            </div>
            <div className="text-center md:text-right">
              <p className="text-sm text-gray-400">
                © 2024 HVAC Dr. All rights reserved.
              </p>
              <p className="text-sm text-gray-400">
                Serving Crittenden County, Arkansas
              </p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App


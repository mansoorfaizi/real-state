# Real Estate API

## Description

A Django-based REST API for managing real estate properties. This application provides a comprehensive backend solution for handling various types of real estate listings, including houses, apartments, offices, and lands. It supports multiple deal types such as sale, rent, and mortgage, with detailed specifications for each property type.

## Features

- **Comprehensive Property Management**: Support for multiple property types (houses, apartments, offices, lands) with type-specific attributes
- **Flexible Deal Types**: Handle sale, rent, and mortgage transactions
- **Geographic Organization**: Hierarchical location system with provinces, districts, and areas
- **Media Integration**: Attach media files and captions to property listings
- **Multi-Currency Support**: Handle pricing in different currencies
- **Review System**: Allow users to leave reviews for properties
- **Detailed Specifications**: Extensive attributes for each property type including amenities, measurements, and features

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 5.2

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd real-state
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## Usage

### API Endpoints
*Note: API views are not yet implemented. This is currently a model-only setup. Endpoints need to be developed using Django REST Framework or similar.*

### Data Models

#### Core Models
- **Property**: Base model containing common property information
  - Title, deal type (sale/rent/mortgage), property type, location, pricing, description, coordinates

- **PropertyMedia**: Media attachments for properties
  - File references and captions

#### Property Type Models
- **Apartment**: Specific attributes for apartment listings
  - Floor number, bedrooms, bathrooms, area, balcony, elevator, parking, heating, security, building management

- **House**: Detailed house specifications
  - Bedrooms, bathrooms, total/built area, floors, water type, parking, heating, electricity, official documents

- **Office**: Office space details
  - Area, floor number, rooms, internet, parking, security, toilet type

#### Supporting Models
- **Area, District, Province**: Geographic hierarchy for location management
- **Currency**: Currency definitions for pricing
- **Review**: User reviews and ratings
- **Timestamp**: Base model providing created/updated timestamps

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
Follow Django's coding standards and use meaningful commit messages.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Contact

For questions or support, please open an issue in the repository.

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Booking, Listing
from datetime import datetime



class Command(BaseCommand):
    help = 'Seed Database with initial data for testing purposes'

    def handle(self, *args, **options):
        User = get_user_model
        self.stdout.write('Seeding database...')
        try:
            user = User.objects.create_user(username='testuser', password='password123')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating user: {e}'))
            return

        listing = Listing.objects.create(
            title='Cozy Cottage',
            description='A cozy cottage in the countryside.',
            location='Countryside',
            price_per_night=100.00,
            host=user
        )

        
        start_date = datetime(2023, 10, 1).date()
        end_date = datetime(2023, 10, 5).date()
        total_price = (end_date - start_date).days * listing.price_per_night

        Booking.objects.create(
            listing=listing,
            guest=user,
            start_date='2023-10-01',
            end_date='2023-10-05',
            total_price=total_price
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
        self.stdout.write('Created user: testuser')
        self.stdout.write(f'Created listing: {listing.title}')
        self.stdout.write(f'Created booking for {user.username} at {listing.title}')
        self.stdout.write(f'Start date: {start_date}, End date: {end_date}, Total price: ${total_price}')
        self.stdout.write('Done seeding database.')
        return
        
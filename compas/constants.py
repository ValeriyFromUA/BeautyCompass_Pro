import os

from dotenv import load_dotenv

load_dotenv()
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
SECRET = os.environ.get('SECRET')

RENDER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)
PAGE_SIZE = 5
ACCESS_TOKEN_LIFETIME = 5  # minutes
REFRESH_TOKEN_LIFETIME = 1  # days

CATEGORIES = ['Acne Treatment',
              'Aestheticians',
              'Barbers',
              'Beauty & Spas',
              'Blow Dry/Out Services',
              'Body Contouring',
              'Cosmetic Surgeons',
              'Cosmetics & Beauty Supply',
              'Cosmetology Schools',
              'Day Spas',
              'Dermatologists',
              'Eyebrow Services',
              'Eyelash Service',
              'Float Spa',
              'Hair Extensions',
              'Hair Loss Centers',
              'Hair Removal',
              'Hair Salons',
              'Hair Stylists',
              'Health & Medical',
              'Hydrotherapy',
              'Laser Hair Removal',
              'Makeup Artists',
              'Massage',
              'Massage Therapy',
              'Medical Spas',
              'Nail Salons',
              'Permanent Makeup',
              'Piercing',
              'Skin Care',
              'Tanning',
              'Tattoo Removal',
              'Teeth Whitening',
              'Threading Services',
              'Waxing',
              'Wigs']

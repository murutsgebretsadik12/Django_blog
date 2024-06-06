

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build script completed successfully."
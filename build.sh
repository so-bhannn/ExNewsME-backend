echo "BUILD START"
python3.9 -m pip install -r requiremnts.txt
python3.9 -c "from my_script import generate_secret_key; print(generate_secret_key())" > secret_key.txt
export DJANGO_SECRET_KEY=$(cat secret_key.txt)
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
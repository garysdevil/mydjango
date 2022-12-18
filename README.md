```bash
# - https://github.com/openai/openai-python

venv_name="python_openai_venv"
python3 -m venv ~/devenv/${venv_name}
source ~/devenv/${venv_name}/bin/activate
pip3 install Django==4.1.4
# pip3 install openai==0.25.0
pip3 install --upgrade openai

echo "OPENAI_API_KEY=YOUR_OPENAI_API_KEY" >> .env

python3 manage.py runserver 127.0.0.1:8000

curl 127.0.0.1:8000/openai/chat?prompt="hi"
```
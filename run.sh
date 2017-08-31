export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
eval "python -V"
eval "source /media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/tools/pyenv/3.6.1/venv/webapp/bin/activate"
eval "python app.py"
eval "xdg-open http://localhost:5000"


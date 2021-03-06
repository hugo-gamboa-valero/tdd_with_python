import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = "https://github.com/hugo-gamboa-valero/tdd_with_python.git"

def deploy(area):
   site_folder = f"/home/{env.user}/tdd_with_python/sites/{area}"
   run(f"mkdir -p {site_folder}")

   with cd(site_folder):
      get_latest_source()
      update_virtualenv()
      create_or_update_dotenv()
      update_static_files()
      update_database()

def get_latest_source():
   if exists(".git"):
      run("git fetch")
   else:
      run(f"git clone {REPO_URL} .")
   current_commit = local("git log -n 1 --format=%H", capture=True)
   run(f"git reset --hard {current_commit}")

def update_virtualenv():
   if not exists("virtualenv/bin/pip"):
      run(f"python3.6 -m venv virtualenv")
   run("./virtualenv/bin/pip install -r requirements.txt") 

def create_or_update_dotenv():
   append(".env", "DJANGO_DEBUG_FALSE=y") 
   current_contents = run("cat .env")

   if "DJANGO_SECRET_KEY" not in current_contents:
      new_secret = ''.join(random.SystemRandom().choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50))
      append(".env", f"DJANGO_SECRET_KEY={new_secret}")

def update_static_files():
   run("./virtualenv/bin/python manage.py collectstatic --noinput")

def update_database():
   run("./virtualenv/bin/python manage.py migrate --run-syncdb --noinput")




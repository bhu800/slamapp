👍🎉 First off, thanks for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing to SlamApp, which is currently hosted on pythonanywhere server but will be hopefully moved to sntc server of IIT Mandi soon. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Project SetUp
```bash
$ # Get the code
$ git clone https://github.com/fiterace/slamapp.git
$ cd slamapp
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000
```
__Note__ : For login you have to add google oauth credentials. Visit the [Google API Console](https://console.developers.google.com/) to obtain OAuth 2.0 credentials - client ID and client secret and configure them in admin page as explained in this [tutorial](https://wsvincent.com/django-allauth-tutorial-custom-user-model/).
For more info on what else you can do with django-allauth library you can visit https://django-allauth.readthedocs.io/

## How to Contribute ?
1. Fork this repository to your github account.  
2. Clone the forked repository.    
`git clone https://github.com/fiterace/slamapp.git`  
3. Create a new branch.    
`git checkout -b NewBranchName`  
4. Make your changes.  
5. Stage the changes.    
`git add path/to/changed-files`  
6. Commit your changes.    
`git commit -m "Appropriate Commit Message"`  
7. Push your Changes    
`git push origin NewBranchName`  
8. Create a Pull request  
9. Mention someone to review it.  
10. Celebrate your Contribution 🚀 

__In case You want to contribute to this project, here is a little list of features, we are planning to implement in future. Try your hands on anyone of these and hit a Pull Request! Or have yor own idea! Feel free to suggest your ideas or report a bug in issues or drop us a mail at `b18012@students.iitmandi.ac.in` (Bhumanyu Goyal) or `b18123@students.iitmandi.ac.in` (Naman Tayal).__

## Task-List
- [x] Basic Slam Book app
- [ ] Add custom slambook creation `Create Slam` feature
- [ ] Add notification feature
- [ ] Add invite link sending feature
- [ ] `Add Memories` (image/video file) uploading feature
- [ ] Add Slam Book `Download` feature ( A soft copy of Slams will be available for download after slambook filling period.)
- [ ] Add `Drop in Graffiti` feature (Feel like dropping a few words about someone? Drop in a GRAFFITI.)
- [ ] Social Profile feature (User profiles can be filled, updated and browsed)
- [ ] Public/Private option in profile (An option in 'Edit Profile' to make SLAMBOOK public or private according to your convenience. The default setting will be 'Public'.)

Thanks! ❤️ ❤️ ❤️  
Bhumanyu Goyal, Naman Tayal  
Literary Society, IIT Mandi

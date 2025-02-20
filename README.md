# Web Site Builder

This is a simple project that looks like Linktree, but in Django, that's not complete like it, but at least Iunderstood about color and image fields.

## Executing

First, download this project, then, using a virtual environment run the command:

```
pip install django django-colorfield Pillow
```

Finally, run to execute: 

### Unix/Mac OS:

```
python3 manage.py runserver
```

### Windows:

```
py manage.py runserver
```

## How it works

To create a site, go to the admin site and add a Site.

You'll have to define the color of the text, the background, the title, the description and the logo. You can also define your Instagram, the X, and the Facebook.

To add new links, add a Link, and change the description, the URL and  select your site.

Now, when you add `sites/` and the site name, you get in your site, showing everything you told to the admin page.


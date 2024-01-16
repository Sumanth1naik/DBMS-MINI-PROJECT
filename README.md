Welcome to our Crowdfunding Web App, a dynamic platform designed to empower individuals and organizations to bring their innovative ideas and projects to life. Our application provides a user-friendly and secure environment for creators to showcase their initiatives and for backers to support causes they are passionate about. Whether you're a startup, artist, or community organizer, our platform is the bridge that connects visionaries with the community eager to make a positive impact.

**Configuration steps**
1. Make sure you have django installed in your system
2. install all the library
3. After all the installation *py manage.py runserver* use this command to run the project


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Django Commands</title>

</head>
<body>

  <h2>Django Commands</h2>

  <ol>
    <li>
      <code>django-admin startproject projectname</code>
      <p>Initializes a new Django project with the specified name.</p>
    </li>
    <li>
      <code>cd projectname</code>
      <p>Changes the current working directory to the Django project directory.</p>
    </li>
    <li>
      <code>python manage.py startapp appname</code>
      <p>Creates a new Django app within the project.</p>
    </li>
    <li>
      <code>python manage.py migrate</code>
      <p>Applies pending database migrations to update the database schema.</p>
    </li>
    <li>
      <code>python manage.py createsuperuser</code>
      <p>Prompts to create a superuser account for admin-level access.</p>
    </li>
    <li>
      <code>python manage.py runserver</code>
      <p>Launches the Django development server (default: <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>).</p>
    </li>
    <li>
      <code>python manage.py makemigrations</code>
      <p>Creates new database migrations based on changes to models.</p>
    </li>
    <li>
      <code>python manage.py migrate appname</code>
      <p>Applies app-specific migrations to update the database.</p>
    </li>
  </ol>

</body>
</html>

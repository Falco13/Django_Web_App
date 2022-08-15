# Web application - Django + REST API

- User model with registration implemented.
- When a user is registered, the user is prompted for a username, email and password. And also - a short biography, and date of birth.
- Authorization of the User is possible with Username or Email, for this the method authenticate() is overridden.
- The Post model is implemented, any User can create a Post - with the post topic, description and attached photo to it.
- The Home page of the site displays all created posts of users by the time of publication.
- Added the ability to comment on posts (any authorized user can comment) on the main page + added a comment counter.
- The superuser (admin) has the right to delete any post and comment in the Admin-page, + added the ability to hide unwanted comments.

Class based views used. (CBV).

__Also added API end-points:__
- api/posts
- api/users
- api/users/id


__Used tools:__    
:heavy_check_mark: Python    
:heavy_check_mark: Django [web framework]   
:heavy_check_mark: Django REST Framework    
:heavy_check_mark: HTML+CSS+Bootstrap    
:heavy_check_mark: SQLite database    
:heavy_check_mark: Pillow    

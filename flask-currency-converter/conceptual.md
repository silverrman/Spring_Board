# Flask Currency Converter - Conceptual Questions

### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  
  Python and JavaScript differ in several important ways:
  * **Execution environment**: Python typically runs server-side, while JavaScript was traditionally client-side (browsers) but now also runs server-side (Node.js)
  * **Types**: Python uses strong, dynamic typing while JavaScript uses weak, dynamic typing
  * **Syntax**: Python uses indentation for code blocks and emphasizes readability, while JavaScript uses braces and semicolons
  * **Concurrency**: JavaScript is single-threaded with asynchronous capabilities through promises/async-await, while Python has multiple concurrency models (threads, processes, asyncio)
  * **Libraries**: Python has extensive libraries for scientific computing, data analysis, and machine learning, while JavaScript's ecosystem is centered around web development
  * **Object system**: JavaScript uses prototype-based inheritance, while Python uses class-based inheritance

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.
  
  1. Using the `get()` method: `my_dict.get("c", default_value)` - Returns the default value if the key doesn't exist
  2. Using a try/except block:
     ```python
     try:
         value = my_dict["c"]
     except KeyError:
         value = default_value
     ```

- What is a unit test?
  
  A unit test is a type of software testing where individual units or components of the software are tested in isolation. The purpose is to validate that each unit of the software performs as designed. In Python, a unit typically refers to a function, method, or class. Unit tests are typically automated, quick to run, and focus on testing a specific piece of functionality without dependencies on external systems.

- What is an integration test?
  
  An integration test verifies that different modules or services used by your application work well together. Unlike unit tests that isolate components, integration tests evaluate multiple components working together. For example, an integration test might verify that your application correctly interacts with a database, file system, or external API. These tests are important to catch issues that might not be apparent when testing components in isolation.

- What is the role of web application framework, like Flask?
  
  A web application framework like Flask provides a structured way to build web applications by offering tools, libraries, and patterns. Flask's role includes:
  * Handling HTTP requests and generating responses
  * URL routing to map URLs to specific functions/views
  * Template rendering for generating dynamic HTML
  * Session and cookie management
  * Integration with databases and other extensions
  * Security features like CSRF protection
  * Simplified development through conventions and pre-built components
  
  Flask specifically is a "micro" framework that provides core functionality while allowing developers to choose which components to add based on their needs.

- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?
  
  * **Route parameters** are better for:
    - Required information that identifies a resource (IDs, slugs, names)
    - Hierarchical data that represents the structure of your resources
    - RESTful API design where the URL represents the resource
    - Data that is essential to the page/view being loaded
    - Example: `/users/42` or `/products/electronics/laptops`
  
  * **Query parameters** are better for:
    - Optional parameters or filters
    - Sorting, pagination, or filtering data
    - Search functionality
    - Non-hierarchical data that doesn't define the resource
    - Example: `/products?category=electronics&sort=price&page=2`

- How do you collect data from a URL placeholder parameter using Flask?
  
  In Flask, you define route parameters with angle brackets in the route definition and receive them as arguments to the view function:
  
  ```python
  @app.route('/user/<username>')
  def show_user_profile(username):
      # username variable contains the value from the URL
      return f'User: {username}'
  ```
  
  You can also specify the type of the parameter:
  
  ```python
  @app.route('/post/<int:post_id>')
  def show_post(post_id):
      # post_id will be converted to an integer
      return f'Post ID: {post_id}'
  ```

- How do you collect data from the query string using Flask?
  
  Query string parameters can be accessed through the `request.args` multidict:
  
  ```python
  from flask import request
  
  @app.route('/search')
  def search():
      query = request.args.get('q', '')  # Default to empty string if 'q' is not provided
      page = request.args.get('page', 1, type=int)  # Convert to integer with default of 1
      return f'Search for: {query}, Page: {page}'
  ```

- How do you collect data from the body of the request using Flask?
  
  For form submissions, you can access form data using `request.form`:
  
  ```python
  from flask import request
  
  @app.route('/submit', methods=['POST'])
  def submit():
      username = request.form.get('username')
      password = request.form.get('password')
      return f'Form submitted with username: {username}'
  ```
  
  For JSON data (common in APIs), you use `request.get_json()`:
  
  ```python
  @app.route('/api/data', methods=['POST'])
  def process_data():
      data = request.get_json()
      name = data.get('name')
      return f'Received name: {name}'
  ```
  
  For file uploads, you use `request.files`:
  
  ```python
  @app.route('/upload', methods=['POST'])
  def upload_file():
      uploaded_file = request.files.get('file')
      if uploaded_file:
          uploaded_file.save('/path/to/save/' + uploaded_file.filename)
      return 'File uploaded'
  ```

- What is a cookie and what kinds of things are they commonly used for?
  
  A cookie is a small piece of data sent from a website and stored on the user's browser. Cookies are commonly used for:
  
  * **Session management**: Keeping users logged in, maintaining shopping carts
  * **Personalization**: Storing user preferences, themes, or settings
  * **Tracking**: Analyzing user behavior and patterns for analytics
  * **Advertising**: Tracking users across websites for targeted advertising
  
  In Flask, you can set cookies using the response object:
  
  ```python
  from flask import make_response
  
  @app.route('/set-cookie')
  def set_cookie():
      resp = make_response('Cookie set!')
      resp.set_cookie('user_id', '12345', max_age=3600)  # Expires in 1 hour
      return resp
  ```
  
  And read cookies using `request.cookies`:
  
  ```python
  from flask import request
  
  @app.route('/get-cookie')
  def get_cookie():
      user_id = request.cookies.get('user_id')
      return f'User ID from cookie: {user_id}'
  ```

- What is the session object in Flask?
  
  The session object in Flask is a way to store information specific to a user from one request to the next. Unlike cookies that store data on the client-side, Flask sessions use a signed cookie to store session data on the client but are cryptographically signed so users cannot modify the data. This makes it more secure than using regular cookies.
  
  Sessions are commonly used for:
  * User authentication state (keeping track of logged-in users)
  * Temporary message storage (flash messages)
  * Shopping carts or multi-step form data
  * User preferences during the current session
  
  Example of using sessions in Flask:
  
  ```python
  from flask import session
  
  app.secret_key = 'your_secret_key'  # Required for sessions to work
  
  @app.route('/login')
  def login():
      session['user_id'] = 42
      return 'Logged in!'
  
  @app.route('/profile')
  def profile():
      if 'user_id' in session:
          return f'User ID in session: {session["user_id"]}'
      return 'Not logged in', 401
  
  @app.route('/logout')
  def logout():
      session.pop('user_id', None)
      return 'Logged out!'
  ```

- What does Flask's `jsonify()` do?
  
  Flask's `jsonify()` function converts a Python object (like a dictionary, list, or other serializable type) into a JSON response object with the appropriate content type and headers. This is especially useful for building APIs where responses need to be in JSON format. The function:
  
  * Converts Python objects to JSON format
  * Sets the response MIME type to `application/json`
  * Handles Unicode and other serialization details
  * Returns a `Response` object that can be returned from a view function
  
  Example usage:
  
  ```python
  from flask import jsonify
  
  @app.route('/api/users')
  def get_users():
      users = [
          {'id': 1, 'name': 'Alice'},
          {'id': 2, 'name': 'Bob'}
      ]
      return jsonify(users)
  
  @app.route('/api/user/<int:user_id>')
  def get_user(user_id):
      # Get user data from database...
      user = {'id': user_id, 'name': 'Example User'}
      return jsonify(user)
  ```

## GamePedia:

### **Distinctiveness and Complexity:**
GamePedia is a web application designed to facilitate decision-making for gamers when choosing which games to play. The platform allows users to access and contribute opinions on various video games, aiding others in making informed decisions about their gaming investments. Developed using a combination of web technologies, the project incorporates HTML, CSS, Django templates, models, and forms. The inclusion of JavaScript enables the creation of a custom API, facilitating asynchronous updates and dynamic content changes. The project features a robust and efficient database structure, offering a more intricate system compared to previous projects. With practical utility for gamers worldwide, GamePedia provides valuable insights into the gaming community's collective opinions.

### **Documentation:**
**layout:** The layout page serves as the foundation for utilizing Bootstrap and includes the navigation bar used across all pages.

**NavBar:** The navigation bar offers links such as 'GamePedia,' 'Login,' and 'Genres' for users. Depending on the user's status, the 'Login' link may be replaced with their username if the user is loged-in. Additional links include 'Playlists' to view saved games, 'Add a Game' to contribute to the database, and 'Unverified Games' for staff members.

**Home Page:** The main page displays top-rated games and features a search bar for easy game discovery. JavaScript communicates with the database through a custom API, enabling users to click on game cards or titles to access the respective game page.

**Game Page:** Each game page consists of three sections: Info, User Rating, and Others' Rating. The Info Section provides details about the game, while the User Rating Section allows signed-in users to submit their reviews. The Others' Rating Section showcases reviews from other users.

**Add a Game:** The 'Add a Game' page includes a form for users to contribute new games to the database. The form covers various details, including Title, Image, Description, Release Date, Genres, Developer, and Publisher.

**Genres:** Clicking on the 'Genres' link leads users to a page displaying genre cards. Selecting a genre card reveals all games within that genre, offering a convenient way to explore specific genres.

**Developer:** Clicking on a developer's name displays a page featuring games developed by that specific developer.

**Playlist:** Users can add games to their playlist from each game page. Clicking the 'Playlist' link in the navigation bar redirects users to a personalized page displaying their saved games.

**Login and Create Account:** The login page includes options to log in or create a new account. The 'Create Account' link asynchronously replaces the login form with a registration form.

**Staff Members:** Staff members have access to an 'Unverified Games' link, leading to a page displaying games with unverified status. Staff members can review, verify, or delete games.

**Mobile-Responsivity:** The web app is fully mobile-responsive, tested on various devices to ensure optimal display across different screen sizes.

## How to Run:
To run the web app, execute the following command in the terminal from the main project directory: '**python manage.py runserver**,' and access the provided link using any web browser.
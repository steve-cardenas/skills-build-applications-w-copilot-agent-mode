# Build Applications with GitHub Copilot Agent Mode

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey steve-cardenas!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/steve-cardenas/skills-build-applications-w-copilot-agent-mode/issues/1)

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)


Let's setup codespace for the URL, start the server via VS Code launch.json, and test the API.

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.
- Only update urls in `settings.py` and `urls.py`
- REST api endpoint format https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
- example full url: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
- Do not hard code the `$CODESPACE_NAME` value use the variable
- Do not update the `views.py`

1. Update `urls.py` to replace the return for the REST API URL endpoints with the environment variable $CODESPACE_NAME https://$CODESPACE_NAME-8000.app.github.dev for Django and avoid certificate HTTPS issues.
2. Make sure the Django backend works on your codespace URL and localhost (i.e., the value of `$CODESPACE_NAME`) by updating `ALLOWED_HOSTS` in `settings.py`.
3. Test the API endpoints using curl command.


Let's setup the octofit-tracker frontend React  framework and
ensure everything is created in the `octofit-tracker/frontend` directory by using `--prefix`

1. Make sure the the octofit-tracker/frontend directory exists.
2. create the react app
3. Install react, bootstrap, and react-router-dom
4. Import bootstrap css in the src/index.js file.
5. Don't change .gitignore file


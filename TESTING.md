# Testing

This document records both automated and manual testing for the Crow project. It was expanded after assessor feedback to provide clear evidence of functionality, usability, responsiveness, JavaScript behaviour, and data handling.

## Testing Strategy

The testing approach for this project includes:
- automated Django tests for core authentication, CRUD, and permission rules;
- manual feature testing for all major user flows;
- JavaScript and UI testing for voting, dropdowns, and search interactions;
- responsiveness checks across device sizes;
- validator and linting checks;
- bug tracking and fixes.

## Automated Python Testing

Automated Django tests were added to provide baseline regression coverage.

### Accounts tests

File: `accounts/tests.py`

Covered areas:
- registration page loads successfully;
- user can register with valid data;
- login page loads successfully.

### Posts tests

File: `posts/tests.py`

Covered areas:
- home page renders;
- authenticated user can create a post;
- unauthenticated user is redirected from the protected create route;
- post author can edit their own post;
- non-author cannot edit another user's post;
- post author can delete their own post;
- authenticated user can add a comment;
- users can vote on a post;
- search returns an expected result;
- profile page loads for a valid user.

### Running tests locally

```bash
python manage.py test
```

## Manual Testing Matrix

| Feature | Test Steps | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Register account | Open Register page, enter valid username/password, submit | User account created successfully | Pass |
| Login | Open Login page, enter valid credentials, submit | User is logged in and navbar updates | Pass |
| Logout | Click Logout | User is logged out and restricted actions disappear | Pass |
| Home feed load | Visit home page as guest | Feed renders without error | Pass |
| Create post access control | Visit create URL as guest | Redirect to login page | Pass |
| Create post without file | Log in, add title/content/category, submit | Post saved successfully and feedback shown | Pass |
| Create post with image | Upload one valid image and submit | Post saved and image displayed correctly | Pass |
| Create post with PDF | Upload one valid PDF and submit | Post saved and file displayed as document link/card | Pass |
| Create post with TXT file | Upload one valid TXT file and submit | Post saved and file displayed as document link/card | Pass |
| Create post with empty file input | Submit create form with no real file selected in an upload field | Application does not crash | Pass |
| Edit own post | Log in as author, update post, save | Post updates successfully | Pass |
| Edit another user's post | Log in as non-owner and open edit URL | Access is blocked | Pass |
| Delete own post | Log in as author and delete post | Post removed successfully | Pass |
| Delete another user's post | Log in as non-owner and open delete URL | Access is blocked | Pass |
| View post detail | Open post detail page | Correct post details load | Pass |
| Add comment | Submit a comment while logged in | Comment appears on the post | Pass |
| Reply to comment | Submit a reply to an existing comment | Reply appears under parent comment | Pass |
| Edit own comment | Open edit comment page and save changes | Comment updates successfully | Pass |
| Delete own comment | Delete comment as author | Comment removed successfully | Pass |
| Vote up | Click upvote as authenticated user | Score updates correctly | Pass |
| Vote down | Click downvote as authenticated user | Score updates correctly | Pass |
| Toggle same vote | Click same vote twice | Vote removed and score updates back | Pass |
| Search results | Type a matching keyword in search bar | Matching posts appear in dropdown | Pass |
| Search close behaviour | Click outside search area | Dropdown closes without console errors | Pass |
| Navbar profile menu | Click profile button | Menu opens and closes correctly | Pass |
| Create-page toast message | Create a post successfully | Toast appears on create page and auto-hides | Pass |
| Home flash auto-hide | Trigger home flash message | Flash message fades after short delay | Pass |
| Responsive layout | Resize browser to mobile/tablet/desktop widths | Layout remains usable and readable | Pass |
| Broken internal links | Navigate all main pages | No broken internal links found | Pass |

## JavaScript Testing

The project includes several interactive JavaScript behaviours that were manually tested.

### Voting system

- verified score updates without a full page reload;
- verified toggling the same vote removes it;
- verified switching vote direction updates score correctly.

### Search dropdown

- verified results show when typing a matching query;
- verified dropdown hides when query is cleared;
- verified dropdown closes when clicking outside the search area;
- verified the script uses the correct `.search-box` selector.

### Navbar menu

- verified profile dropdown opens on click;
- verified profile dropdown closes when clicking elsewhere;
- fixed selector mismatch so the script correctly targets `.nav-profile-btn`.

### Create post page

- verified create-page toast messages appear after submit;
- verified toast messages auto-hide after a short delay;
- verified document uploads no longer render as broken images;
- verified empty upload fields do not crash the application.

## Responsiveness Testing

Manual checks were completed using browser developer tools and browser resizing.

Tested breakpoints:

- mobile;
- tablet;
- desktop.

Checked areas:

- navbar layout;
- home feed card spacing;
- post detail media layout;
- create and edit form layout;
- profile page layout.

Result: the layout remained functional and readable across tested sizes.

## Browser Testing

The application was manually checked in:

- Google Chrome;
- Microsoft Edge.

Result: core features behaved as expected in tested browsers.

The live deployed version was also checked after Heroku deployment to confirm that the hosted environment matched local expectations for core navigation, authentication, post creation, and media handling.

## Validation and Linting

### Python

Python files were checked with Flake8 during development.

The code was adjusted to improve line length compliance and readability.

### HTML

Django templates were reviewed after refactoring form rendering.

### CSS

CSS files were reviewed to remove broken lines and improve form/message styling.

### JavaScript

JavaScript files were tested using the browser console.

No blocking console errors remain in the updated interactions.

## Bugs Found and Fixed

| Bug | Status | Notes |
| --- | --- | --- |
| Deployment instructions referenced GitHub Pages instead of Heroku | Fixed | README updated to reflect Heroku deployment |
| Testing evidence missing | Fixed | Added this document and automated tests |
| Navbar script used wrong selector | Fixed | Updated to `.nav-profile-btn` |
| Search script used wrong wrapper selector | Fixed | Updated to `.search-box` |
| Search script not loaded | Fixed | Added script include in navbar template |
| Edit post/comment views bypassed ModelForms | Fixed | Refactored to use Django forms |
| Empty file upload could crash post creation | Fixed | Empty uploads are now guarded |
| PDF and document files displayed as broken images | Fixed | Document detection/rendering improved |
| Success message appeared on home page instead of create page | Fixed | Create flow now redirects back to create page and uses toast feedback |

## Known Limitations

Media behaviour still depends on correct Cloudinary configuration in local and deployed environments.

Automated front-end testing could be expanded further in a future version.

## Conclusion

The Crow project now includes stronger testing evidence in line with PP4 requirements. Manual testing, automated testing, JavaScript behaviour checks, and documented bug fixes collectively support the quality and stability of the application for resubmission.

# Agile Planning

This document records the Agile planning evidence for Crow, including epics, user stories, acceptance criteria, task breakdowns, and MoSCoW prioritisation.

## Agile Method Used

The project followed an iterative Agile workflow:
- identify user and site owner needs;
- group related work into epics;
- refine epics into user stories;
- break user stories into implementation tasks;
- prioritise work using MoSCoW;
- develop features incrementally and review after testing.

## Project Goals

1. Build a community-based social feed using Django.
2. Provide secure authentication and authorisation.
3. Deliver full CRUD functionality for posts and comments.
4. Support rich interaction through voting, replies, media, and search.
5. Deploy securely with production-ready configuration.

## Epics

### Epic 1 – Authentication and access

Registration, login, logout, restricted actions, and authenticated navigation.

### Epic 2 – Post creation and management

Creating, viewing, editing, and deleting posts.

### Epic 3 – Social interaction

Comments, replies, and voting.

### Epic 4 – Discovery and usability

Search, profile views, responsive layout, and navigation clarity.

### Epic 5 – Deployment, testing, and documentation

Secure deployment, README quality, testing evidence, and project documentation.

## User Stories

### Must Have

#### US01 – Register account

As a visitor, I want to create an account so that I can participate in the platform.

**Acceptance criteria**
- A registration form is available.
- Valid details create a new account.
- The user can then log in.

#### US02 – Log in and log out

As a registered user, I want to log in and log out so that I can access protected features securely.

**Acceptance criteria**
- The login form accepts valid credentials.
- Invalid credentials are rejected.
- Logout ends the authenticated session.

#### US03 – Create post

As an authenticated user, I want to create a post so that I can share content with the community.

**Acceptance criteria**
- Logged-in users can access the create post page.
- A valid form creates a post.
- Success or error feedback is shown clearly.

#### US04 – View feed and post details

As a visitor, I want to browse posts so that I can discover content without needing an account.

**Acceptance criteria**
- The home page displays posts.
- Users can open post detail pages.
- The layout remains clear and responsive.

#### US05 – Edit own post

As a post author, I want to edit my own post so that I can correct or improve it.

**Acceptance criteria**
- Only the author can access edit functionality.
- Existing data is pre-filled.
- Saved changes are reflected immediately.

#### US06 – Delete own post

As a post author, I want to delete my own post so that I can remove unwanted content.

**Acceptance criteria**
- Only the author can delete the post.
- The user is redirected after deletion.
- The post no longer appears in the feed.

#### US07 – Comment on a post

As an authenticated user, I want to comment on a post so that I can join the discussion.

**Acceptance criteria**
- Logged-in users can submit comments.
- New comments appear on the post detail page.
- Guests cannot perform restricted comment actions.

#### US08 – Reply to a comment

As an authenticated user, I want to reply to another comment so that threaded conversations are possible.

**Acceptance criteria**
- The reply is linked to the parent comment.
- Replies appear beneath the correct comment.
- Only authenticated users can submit replies.

#### US09 – Vote on a post

As an authenticated user, I want to upvote or downvote posts so that I can express interest or disagreement.

**Acceptance criteria**
- Users can cast one vote per post.
- Repeating the same vote removes it.
- The score updates correctly.

### Should Have

#### US10 – Search posts

As a visitor, I want to search the platform so that I can quickly find content.

**Acceptance criteria**
- Typing a query returns matching results.
- Results are relevant to titles or authors.
- The dropdown can be closed cleanly.

#### US11 – View profile page

As a visitor, I want to view a user profile so that I can see their public contributions.

**Acceptance criteria**
- Profile pages load for valid users.
- User posts are displayed correctly.
- Invalid usernames are handled appropriately.

#### US12 – Responsive layout

As a user on any device, I want the platform to remain usable so that I can browse and interact comfortably.

**Acceptance criteria**
- Navigation remains usable on smaller screens.
- Feed cards do not overlap or overflow.
- Forms remain readable and usable across device sizes.

### Could Have

#### US13 – Category suggestion help

As a content creator, I want category suggestions so that tagging posts is easier.

#### US14 – Improved media viewing

As a user, I want a smoother media-viewing experience so that browsing uploads feels more polished.

## MoSCoW Prioritisation Summary

### Must Have

- Registration and login
- Auth-aware navigation
- Post CRUD
- Commenting and replies
- Voting
- Permission enforcement
- Responsive layouts

### Should Have

- Search
- Profile pages
- Additional usability refinements

### Could Have

- Category suggestion improvements
- More advanced gallery and document display enhancements

### Won't Have in this iteration

- Follow system
- Notifications
- Bookmarks
- Moderator dashboard

## Epic to Story to Task Example

**Epic:** Post creation and management  
**User Story:** As an authenticated user, I want to create a post so that I can share content.  
**Tasks:**
- build the create form;
- validate required fields;
- save the author automatically;
- support optional media uploads;
- display feedback after submission.

## Mapping to Final Project

- Authentication epic maps to account routes and navbar state.
- Post management epic maps to create, edit, delete, and detail views.
- Social interaction epic maps to comments, replies, and votes.
- Discovery epic maps to search, profiles, and responsive feed views.
- Deployment, testing, and documentation epic maps to README.md, TESTING.md, UX.md, deployment steps, and security/deployment clarity.

## Conclusion

The original repository did not clearly present enough Agile evidence. This document addresses that gap by explicitly recording epics, user stories, acceptance criteria, prioritisation, and implementation structure for the final resubmission.

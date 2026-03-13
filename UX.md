# UX Design Notes

This document expands on the design reasoning behind Crow and supports the README.

## Target Audience

Crow is aimed at users who want a lightweight and familiar discussion platform where they can:
- share short posts quickly;
- browse community content easily;
- interact through votes, comments, and replies;
- use the site comfortably across device sizes.

## UX Goals

The main UX goals were:
- make the purpose of the site obvious immediately;
- reduce cognitive load through a familiar feed layout;
- make primary actions easy to find;
- provide clear feedback after user actions;
- support both guest and authenticated users without confusion.

## Information Hierarchy

The information hierarchy was planned as follows:
1. Navigation first.
2. Feed content second.
3. Social actions third.
4. Supporting metadata last.

## Layout Decisions

### Navigation

A top navigation bar keeps core actions easy to access:
- Home
- Create Post
- Search
- Login / Register or Profile / Logout

### Feed cards

Posts are displayed in card-style blocks because this is a familiar and scannable social-platform pattern.

### Detail view

A dedicated post detail page allows comments and replies to be displayed without overcrowding the main feed.

### Create and edit pages

Separate create and edit pages reduce clutter and make form handling clearer, especially when media uploads are involved.

## User Control and Feedback

The project aims to keep users in control by:
- restricting edit and delete actions to content owners;
- showing visible success and error messages;
- using immediate UI feedback for actions such as voting;
- avoiding aggressive autoplay or disruptive interactions.

## Accessibility Considerations

The project was designed with these accessibility considerations in mind:
- readable contrast between text and background;
- responsive spacing to avoid cramped layouts;
- clear button labels and visible interaction states;
- semantic structure where practical in templates;
- navigation that remains usable on smaller screens.

## Responsive Strategy

The responsive strategy focused on preserving usability rather than simply shrinking content:
- content stacks vertically on smaller screens;
- spacing is reduced without losing readability;
- navigation remains usable across breakpoints;
- forms stay legible and easy to use.

## Media UX Improvements

During resubmission fixes, media handling was improved so that:
- images render as images;
- videos render as videos;
- PDFs and text files render as document links/cards rather than broken previews;
- create-page feedback appears on the create page and auto-hides.

## Future UX Improvements

Possible future UX refinements include:
- clearer empty states for search and profiles;
- richer user profile customisation;
- notification indicators for replies and interactions;
- bookmark and save patterns for content discovery.

## Conclusion

The UX design of Crow intentionally follows familiar community-platform patterns so that users can understand the site quickly. The focus is on clarity, consistency, responsiveness, and confident user interaction.

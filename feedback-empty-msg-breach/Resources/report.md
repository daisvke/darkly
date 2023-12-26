# Message field in the feedback page can be empty

## Description
We identified a security vulnerability in the `Message` input field located at `http://IP/?page=feedback`.<br />
<br />
While the name field undergoes validation, users can submit feedback without filling in the message box.<br />
The flag is revealed when entering single characters such as 'a', 'c', or 'e', without any messages.
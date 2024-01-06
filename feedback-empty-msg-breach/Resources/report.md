# Message field in the feedback page can be empty

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/?page=feedback`

### Issue Description:
While the name field undergoes validation, users can submit feedback without filling in the message box.<br />
The flag is revealed when entering single characters such as 'a', 'c', or 'e', without any messages.

## Immediate Action Required:
It appears that there is a typo in the JavaScript code. The name of the textarea in the HTML form is `mtxtMessage`, but in the JavaScript function `validate_form`, `mtxMessage` is used, without the 't'. As a result, the validation function for the message field is not being executed correctly.<br />
Therefore, correcting the typo by using the correct name `mtxtMessage` in the JavaScript function will resolve the issue.

# Message field in the feedback page can be empty

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/?page=feedback`

### Issue Description:
While the name field undergoes validation, users can submit feedback without filling in the message box.<br />
The flag is revealed when entering single characters such as 'a', 'c', or 'e', without any messages.

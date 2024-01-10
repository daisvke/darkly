# select-injection-breach

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/index.php?page=survey`

### Issue Description:
We have identified a security vulnerability on the survey page related to the select tag. It has come to our attention that the select tag, responsible for holding a value that can be modified by users using the inspector of the web browser, lacks proper protection against overflowing values.<br />
<br />
Upon investigation, it was observed that the select tag allows values beyond the intended range without implementing sufficient constraints. Specifically, when a value surpasses 100,000, an unexpected behavior occurs, leading to the appearance of the flag.

### Potential Exploitation:
This vulnerability poses a potential risk as it may allow users to manipulate the select tag's value beyond the intended limits, potentially causing unintended consequences or exposing sensitive information. 

## Immediate Action Required:
Implement server-side input validation for the select tag to ensure that the values fall within the expected range.

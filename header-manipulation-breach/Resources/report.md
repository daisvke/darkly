# header-manipulation-breach

## Vulnerability Discovery:

### Affected URL: `http://{IP_ADDR}/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f` (link found in the copyright footer)

### Issue Description:
Upon inspecting the source code of the webpage hosted at the provided URL, we discovered a lengthy comment section embedded within a `<section>` tag. Notably, the comment contains the following directives:

- `You must cumming from : "https://www.nsa.gov/" to go to the next step`
- `Let's use this browser : "ft_bornToSec". It will help you a lot.`

Based on our analysis, we infer that these directives pertain to the `User-Agent` and `Referer` headers in the HTTP request. 

## Exploitation Strategy:

### Modifying HTTP Request with Burp Suite:

To verify our hypothesis and exploit the vulnerability, we employed `Burp Suite` to intercept and modify the `HTTP request`. Specifically, we adjusted the following headers:
<br /><br />
BEFORE:
```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36

Referer: http://{IP_ADDR}/index.php?page=survey
```
<br /><br />
AFTER:
```
User-Agent: ft_bornToSec

Referer: https://www.nsa.gov/
```

After forwarding the modified request, we observed that the application behaved differently, revealing the flag, and thus leading us to believe that the vulnerability had been successfully exploited.

## Immediate Action Required:

To address this security vulnerability, we recommend the following immediate actions:

- **Header Validation**: Implement rigorous validation mechanisms for both the User-Agent and Referer headers. Ensure that incoming requests are only processed if they originate from trusted sources.
  
- **Input Sanitization**: Sanitize input parameters, particularly those derived from headers, to prevent unauthorized manipulation and exploitation.
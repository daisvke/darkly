# forgot-pwd-hidden-email-breach

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/index.php?page=recover`

### Issue Description:
Upon careful examination, we discovered that the hidden input tag within the webmaster's password recovery form contains the email address of the webmaster. This oversight presents a potential security loophole that could be exploited by malicious actors.

### Potential Exploitation:
This vulnerability allows an attacker to perform an "email bombing", by creating a loop that continuously sends a large volume of emails to the webmaster's email address. Such an attack could lead to service disruption, overload the email server, and compromise the overall stability of the system.
This directory includes a bash script that can perform such an attack.

## Immediate Action Required:
To mitigate this risk, we recommend the following actions be taken immediately:

### Temporary Disabling of the Form:
	Disable the webmaster recovery form at http://{IP_ADDR}/index.php?page=recover to prevent further exploitation until the vulnerability is addressed.

### Review and Patch the Code:
    Conduct a thorough review of the code associated with the form and implement necessary patches to remove the email address from the hidden input tag.

## Documentation
https://openclassrooms.com/fr/courses/2340511-maitrisez-vos-applications-et-reseaux-tcp-ip/2340656-installez-votre-serveur-smtp

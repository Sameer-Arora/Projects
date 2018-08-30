
## Introduction

TnP Portal which will be a website internal to the college students and facilitate functions like -
Alumni Connect ,Streamlined mails, Internship and placement opportunities ,CV maker, preparation materials and tools for various companies.

## Implementaion Details

### 1- CV Maker 

I have created a portal where the students can create,share ,rate and download the documents most essential for career.As soon as user logins to the portal the session is created which validates the accecss rights to any particular user.

I have created a seperate folder for each user and in each folder three sub-folders cv,coverletter and lom there are only view and download permissions for the other user to other users documents on the server file system.Brief descption of files used are:-

#### Main files:-

1) CV_maker (CV_maker.php):- It contains file where i have made the main editor for the docx files using the tinymce4 editor. One can write his CV,LOM, or other document at that platform.

2) cvmaker_home (cvmaker_home.php,cvmaker_homemain.php):- It contains the main landing page of the cv maker where a person can share,upload,delete and view various cv's sorted department wise and top rated.It also contains the documents personal to the each user which he hasn't shared and those documents are not available for download or viewing purposes. 
 
 Similar files for both cover letter and lom are there.

3) login.php:- It is the main login file which validates the users credentials and dynamically using ajax checks for variosus anomalies . Giving the function of secure loging to the website.

4) logout.php:- It is the site that resets the user state in website by resetting the session variables.

5) session.php:- A php file to handle the sessions accross needed pages.

6) rating.php :- A file to rate the documents uploaded by differnt users.

#### Supporting files:-

1) CV_maker 
	
	i)savedoc.php :- file to save the docx to html and docx and update image stored in the database used the kernel libraries pandoc for this purposes.

2) cvmaker_home:-

	i) upload_cv.php :- file to upload the docx file in the system and creating a thumbnail image and saving in form of docx for further editing.

	ii)delte_cv.php:- file to delete the cv from the file system and from the database.

	iii)share_cv.php:- file to make the cv shareable with others.

	iv)download_cv.php:- file to make the cv donloaded by adding href dynamically to the files.

3) login:-

	i)mailchk.php:-file to send a email with new password for forgor password cases for the already registered users in the portal.


## Technology Used

* I have added all the web technologies from css,html,jquery,ajax,php,javascript,bootstrap in my application.

* The tinyMCE 4 editor to edit the documents online.
* The pandoc library for conversion between formats.
* The dropify add-on to manage files better.
* The slick plugin to manage the display of hundreds of documents. 
* SSMTP PHP mailer to send email to users to verify login and send forgotten passwords.


##

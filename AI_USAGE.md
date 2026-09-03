# AI Usage Documentation

## AI Tool Used

ChatGPT

## Purpose of AI Usage

I used ChatGPT as a development assistant while building this
Python/Django application.

I used it to understand the Django project setup, organize the
application structure, implement the box-selection logic, create
tests, and troubleshoot development issues.

## Prompts Used

The main areas I asked ChatGPT about were:

1. How to create and configure a Django project.
2. How to create Product and Box models.
3. How to implement the box-selection logic.
4. How to create Django views and templates.
5. How to create automated tests.
6. How to troubleshoot template and project setup issues.
7. How to prepare project documentation and test output.

## Accepted AI Outputs

I used AI suggestions for:

- Django project setup.
- Django application structure.
- Product and Box model design.
- Box compatibility checking.
- Box recommendation logic.
- Django view and template structure.
- Automated test structure.
- Project documentation structure.

I reviewed the suggestions and tested the implementation locally.

## Rejected or Modified Outputs

I did not blindly use all generated content.

I reviewed the generated code and modified it when necessary to
match my project structure and requirements.

For example, a template syntax issue was identified and corrected
before the application was tested.

## Mistakes Identified

During development, I encountered an issue in the HTML/Django
template syntax.

The comparison in the template needed to use the correct Django
template syntax:

    {% if selected_product.id == product.id %}

I corrected the template and verified that the product selection
and recommendation page worked correctly.

## Verification Steps

I verified the application through the following steps:

1. Created a Python virtual environment.
2. Installed Django.
3. Created the Django project and application.
4. Ran Django system checks.
5. Created database migrations.
6. Applied database migrations.
7. Created Product and Box records through Django Admin.
8. Tested the web application locally.
9. Tested product and box recommendation.
10. Ran the automated Django test suite.

## Test Verification

The automated test suite was executed using:

    python manage.py test

The test suite found 5 tests and all 5 tests passed successfully.

## Human Review

AI was used as a development assistance tool. I reviewed the
implementation, ran the application locally, tested the
functionality, and verified the automated test results.
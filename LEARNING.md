# What I Learned

While completing this assignment, I learned how to build a web application using Django.

I learned how to create Django models for products and shipping boxes and store their details in a database.

I learned how to implement the box recommendation logic based on product dimensions and weight.

I also learned how to create a Django view and HTML template to allow the user to select a product and see the recommended box.

I learned how to write and run Django test cases and verify that the recommendation logic works correctly.

One challenge I faced was figuring out how to pick the "best" box when more than one box was big enough to fit the product. At first my code just recommended the first box it found that fit, which was not always the most efficient choice. I solved it by calculating the leftover space (unused volume) for every box that fit the product, and then selecting the box with the smallest leftover space instead of just the first match.

I also learned how to use Git and GitHub to manage and submit my project.
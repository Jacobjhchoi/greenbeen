## Inspiration for Green Been
A Yale Research Team found that organic waste occupied the largest percentage of what’s being dumped into landfills. Compost in landfills is not only harmful environmentally, but also economically. For example, it costs New York City over $400 million to collect and dispose the trash it collects, but they could be saving millions as the majority of the trash is actually organic matter. Organic material brought to landfills end up rotting and releasing methane which is not ideal as methane is more than 25 times as potent as carbon dioxide (epa.gov). On the other hand, composting brings carbon to the soil and limits the amount of methane entering air. Getting into composting can be daunting and part of the process is knowing what to compost - Green Been was created to solve this problem.

## What it does
 Green Been uses a custom trained Tensorflow deep learning model to predict whether or not you should compost your item. The user simply uploads an image and Green Been predicts (with nearly perfect accuracy) whether the user should compost their item. The model takes into account many factors, for example, paper can be both composted and recycled, but it is overall more economically/environmentally efficient to recycle.

## How I built it
I built Green Been using 
- Tensorflow to predict whether the user should compost their item
- HTML, CSS, and javascript for the frontend of the page
- Python for backend
- Flask and Heroku for deployment

## Challenges I ran into
I faced many challenged creating this project, some of which include finding good data to train the model, researching how to use Flask to deploy a Tensorflow model, and tuning the model to accurately predict compost/trash.

## Accomplishments that I'm proud of
I am proud to have created a fully functioning web application with an everyday use case that could help both environmentally and economically. I am also proud to have successfully deployed Tensorflow through flask for the first time.

## What I learned
I learned a lot about flask, and how to deploy machine learning models using it. Additionally, I learned how to better use HTML forms, CSS, as well as Manim to create a neural network animation at 0:57 in the video.

## The future of Green Been
Althought Green Been already can be used on IPhones/androids (via the browser), I plan to create an app, so that Green Been will be more easily usable.   Additionally, I plan on further improving the model's accuracy with more fine-tuning/data.

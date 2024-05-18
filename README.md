# Algebrain

An algebra tool to develop visual intuition for solving equations. Intended to be used by GCSE maths students.

***

This tool will (hopefully):

- solve linear equations
- visualise each step of the solving process using manim

This tool could potentially be expanded to visualise other algebra exercises and skills.

***

## Current functionality

In its current form this program rearranges linear equations step by step. It cannot currently factorise, so would not be able to solve `3*x + y*x = 5`. However, it can rearrange equations like `3*(2*y + 5) - x = 4*(3*x + 2)` to make `x` the subject 

## Usage

Input an equation in `main.py`. NOTE: the format must be as follows:

- Spaces between all terms and signs
- products like `3xy` must be written with asterisks, e.g. `3*x*y`

Eventually this will have a gui where you can 'build' an equation so the input formatting is a temporary problem.
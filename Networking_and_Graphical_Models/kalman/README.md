### Main Languages
<p>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white"></p>

### Main Librarys and Modules
<p><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white">
<img src="https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white">
</p>

## kalman - Tracking location and velocity of moving object in n-dimensional space
- **2-dimensional**<br>
  The only information available to us is the initial location (and velocity) and a series of noisy measurements of the velocity as the object moves in space. The key assumption of this problem is that the `true velocity of the object is known to be a constant`. However, the `constant velocity is not known to us`.
  -  Tracked the location (and velocity) of a moving object, e.g. a car, in a 2-dimensional space.
- **3-dimensional**<br>
  Factoring gravity to act on the ball and the intial position as well as the velocities are assumed to be known. Noisy location estimates would be used using a simulated sensor. 
  -  Tracked the location (and velocity) of a moving object, e.g. a ball, in a 3-dimensional space.
  -  Estimated the true location (and velocity) of the ball in 3D space

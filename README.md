# Python-Lab
### Issue
We were having an issue regarding choropleth map not being displayed.<br>
This issue was due to the entire map getting out of the scale of display screen 
to solve this we need to update the code where in the scale must be re-defined by using 
update_goes() function. for example<br>

fig.update_geos(scope="asia") 

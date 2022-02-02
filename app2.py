import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
<html>
<head>
 <style>
 html, body {
	
        width: auto;
        height: auto;
        margin: 0;
        padding: 0 0 0 0;
      }
      .btn {
	  background-color: red;
	  border: none;
	  color: blue;
	  padding: 16px 40px;
	  text-align: center;
	  font-size: 14px;
	  margin: 2px 40px;
	  transition: 0.3s;
	}

.btn:hover {
  background-color: #3e8e41;
  color: white;
}
#dat{
		
              position: absolute;
              top: 250px;
              right: 59px;
               padding: 10px;
               z-index: 400;
			   }
			.btn {width: 70%;} 
#dat1{
		
              position: absolute;
              top: 220px;
              right: 29px;
               padding: 10px;
               z-index: 400;
			   }
			}            
    </style>
</head>
<body>
<table border="0" cellspacing="0" cellpadding="0" border="0">
    <tbody>
        <tr>
            <td width="75" valign="top">
                <table cellspacing="0" cellpadding="0" align="left">
                    <tbody>
                        <tr>
                            <td width="1" height="16">
                                <br/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <br/>
                            </td>
                            <td>
                                <img
                                    src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image001.png"
                                    width="63"
                                    height="96"
                                />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
            <td width="204" valign="top">
                <br clear="ALL"/>
                <p align="left">
                    <a href="https://india.gov.in/hi">
                        <strong>भारत सरकार</strong>
                    </a>
                    <strong></strong>
                
                    <br><a href="https://india.gov.in/">
                        <strong>GOVERNMENT OF INDIA</strong>
                    </a></br>
                    <strong></strong>
                </p>
            </td>
            <td colspan="4" width="463" valign="top">
                <br><p align="center">
                    <strong>विज्ञान</strong>
                    <strong> </strong>
                    <strong>और</strong>
                    <strong> </strong>
                    <strong>प्रौद्योगिकी</strong>
                    <strong> </strong>
                    <strong>मंत्रालय</strong>
                    <strong></strong>
                
                    <br><strong>MINISTRY OF SCIENCE AND TECHNOLOGY</strong>
                </p>
            </td>
            <td colspan="1" width="232" valign="top">
                <p>
                    <img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image004.png"
                        width="241"
                        height="102"
                    />
                </p>
            </td>
            <td  width="232" align="center" valign="middle">
                <p>
                    <img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image006.jpg"
                        width="200"
                        height="107"
                    />
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="7" width="1000" valign="top">
                <p>
                    <strong> </strong>
                </p>
                <p>
                    <strong>
                        Spatial epidemiological modelling of Dengue
						<br>
						using a geospatial approach<br>
						under ICPS program
                    </strong>
                </p>
                
            </td>
        </tr>
		<tr>
            <td colspan="3" rowspan="1" width="538" valign="top">
                <br><p>
                    <img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image008.png"
                        width="106"
                        height="111"
                        border="0"
                    />
                </p>
                <p>
                    <a href="http://www.iitkgp.ac.in/department/AR">
                        Department of Architecture &amp; Regional Planning
                    </a>
                    <br/>
                    <a href="http://www.iitkgp.ac.in">
                        Indian Institute of Technology Kharagpur
                    </a>
                </p>
            </td>
			<td colspan="4" rowspan="5" width="1390" valign="top">
                
            </td>
			<td colspan="2" rowspan="5" width="100" align="top">
             <table>
			     <tr>
				 <td colspan="3" width="285" valign="top">
                <p>
				<br>
				<div id="dat">
                    <form action="">
					<input type="submit" value="Climatic Parameters" name="submit" class="btn">
						
					<br><br>
					<form action="">
					<button value="Analysing Trend" onclick="location.href='https://share.streamlit.io/bhaskar02/display_trend/main/app.py'" type="button" class="btn">
					Analysing Trend
					</button>
						<br><br>
					<form action="">
					<button value="Dengue Hotspots" onclick="location.href='https://share.streamlit.io/bhaskar02/dengueapp/main/bhas1.py?timestamp=1643689888621&page=Bargraph1'" type="button" class="btn">
					Dengue Hotspots
					</button>
					<br><br>
					<form action="">
					
					<button value="Map View" onclick="location.href='http://localhost/sw/Denguefinal1.php'" type="button" class="btn">
					Map View
					</button>
					<br><br>
					<form action="https://ide.geeksforgeeks.org/">
					<button value="Map View" onclick="location.href='new.html'" type="button" class="btn">
					Vector Prevalence
					</button>
					
					</form>
                    
					<br>
					
                  </div>  
                </p>
            </td>
            
            <td width="100" valign="top">
            <p>
            <div id="dat1">
                
				     <img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image010.png"
                        alt="Description: Climatic Parameters"
                        width="80"
                        height="80"
                    />
                    <br>
					<img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image012.png"
                        alt="Description: Analysing Trend"
                        width="80"
                        height="80"
                    />
                    <br>
					<img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image014.png"
                        alt="Description: Dengue Hotspots"
                        width="80"
                        height="80"
                    />
                    <br>
                    <img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image017.png"
                        alt="Description: Earth Globe   Asia"
                        width="80"
                        height="60"
                    />
                    <br>
					<img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image025.png"
                        alt="Description: Bee"
                        width="80"
                        height="60"
                    />
                
                </div>
                </p>
            </td>
             </tr>
             </table>			 
            </td>
			</tr>
			<tr>
			<td colspan="3" width="538" valign="top">
                <br>
				<p>
                    <img
                        src="https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/clip_image019.png"
                        width="118"
                        height="110"
                    />
                </p>
                <p>
                    <a href="https://nimr.org.in">
                        National Institute of Malaria Research, ICMR New Delhi
                    </a>
                    
                    
                </p>
            </td>
			</tr>
			<tr>
            <td colspan="3" width="538" valign="top">
                <br>
				<p>
                    <strong><u>Contact us:</u></strong>
                </p>
            </td>
           </tr>
        <tr>
            <td colspan="3" width="538" valign="top">
                <p>
                    S K Paul
                <br>
                    Department of Architecture &amp; Regional Planning
                <br> Indian Institute of Technology Kharagpur ,India
                </p>
            </td>
        </tr>
        
        
        
    </tbody>
</table>
</body>
<html>

    """,
    width=1000, height=800,
)
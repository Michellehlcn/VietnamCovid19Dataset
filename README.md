<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title>VietNam's Covid19 Dataset</title>
	<link href='default.css' rel="stylesheet" type="text/css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link rel="preconnect" href="https://fonts.googleapis.com"> 
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Lato:wght@700&display=swap" rel="stylesheet">
</head>
<body>
	
	<section class="s1">	
			<div class="header" >
				<div class="header-overlay"></div>
				<div class="header-text">
					<h1>COVID19 VIETNAM</h1>
					<h6>Cases, Vaccinations, Detailed Cases per State & Testing Dataset</h6><p align="center">
						
					</p>
				</div>
			</div>
	</section>

	<section class="s1">
			<div class="description">
				<div class="description-overlay">
				<div class="container">

					<div class="wrapper">
					<div class="left-column">
				
					<br>
					<h4>COVID19 VIETNAM/ COVID-19 tại Việt Nam</h4>
					<p>This page provides a series of dashboards providing the latest information on confirmed COVID-19 cases as well as the latest data on vaccination administration.  All data has been provided by the Ministry of Heath.
					Since the 27th of April 2021, the number of Covid19 cases has seen risen within Bac Giang, Hochiminh City and in Vietnam as a whole. The occurrence of a case of infection in the community with a more transmissible variant of SARS-CoV-2 (Delta variant) and opportunities for wide community exposure, gave me a signal that this wave couldnt be easy to pass by. I have been tracking the data in the middle of May with the new cases per day just below 200. Poorly restrictions and navigation of hotspots, sadly boosted up the transmission not only in southern provinces/states.
					</p>
					<p>The date which information was last updated is noted with the relevant indicators and graphs. <a href="{% url 'posts' %}">Disclaimer</a></p>

					
					<br>
					</div>

					<div class="right-column">
					<p>
					<br>
					<br>	
					<h2>
						Dataset
					</h2>
					<hr>
						<h1>04/08/2021</h1>
					</p>
					<p>Data Last updated</p>
					</div>
				    </div>
				  </div>

				</div>
			</div>
		</section>

	<section class="s1">
		<div class="container">


	<br>


		<div class="row">
			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>New Cases/ Nhiễm</h5>
					<hr>
					<h1 style="color: #8a0303;">7,623 </h1>
				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Local Acquired/ Ca trong nước</h5>
					<hr>
					<h1 style="color: #8a0303;">7,618</h1>
				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Oversea Acquired/ Ca nhập cảnh</h5>
					<hr>
					<h1 style="color: #8a0303;">05</h1>
				</div>
			</div>
		</div>

		<br>
		<div class="row">
			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Confirmed Cases/ Tổng nhiễm</h5>
					<hr>
					<h1 style="color: #8a0303;">177,813</h1>
				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Total Local Cases/ Trong nước</h5>
					<hr>
					<h1 style="color: #8a0303;">175,484</h1>
				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Total Oversea Cases/ Nhập cảnh</h5>
					<hr>
					<h1 style="color: #8a0303;">2,329</h1>
				</div>
			</div>
		</div>

		<br>

		<div class="row">
			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Deceased/ Tử vong</h5>
					<hr>
					<h1 style="color: #8a0303;">2,327</h1>
				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Recoveries/ Khỏi</h5>
					<hr>
					<h1 style="color:#004b6b">54,332</h1>
				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Active Cases/ Đang điều trị</h5>
					<hr>
					<h1 style="color: #8a0303;">121,150</h1>
					
				</div>
			</div>
		</div>
		<br>



		<div class="row">
			<div class="col-md-8">
				<div class="card card-body h-100">
					<h5>New Cases per Province/State</h5>
					<hr>
					<iframe width="100%" height="530" src="https://datastudio.google.com/embed/reporting/3df01d6c-a5ce-438e-ab6c-b95b18567c80/page/FIfWC" frameborder="0"  style="border:0" allowfullscreen Distribute content evenly></iframe>
					</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<table class="table table-striped">
						<thead>
							<tr>
								<th>State</th>
								<th >New</th>
								<th>Change</th>
								<th >Total*</th>
								
							</tr>
						</thead>
						<tbody id="demo"></tbody>
					</table>
					<p style="font-size: 9px;">* The total cases represents the total local acquired cases since 27th of April 2021 - Source from Vnexpress.
					<br>
					** If you can't get the status of the table, Please refresh the page and try again.</p>
				</div>
			</div>
		</div>


		<br>
		<div class="row">
			<div class="col-md-8">
				<div class="card card-body h-100">
					<h5>Vaccines Administered</h5>
				<hr>
				<iframe width="100%" height="530" src="https://datastudio.google.com/embed/reporting/5b0018e5-3507-4a88-8e8f-ebf43d51b9b7/page/p_1j01cg42lc" frameborder="0"  style="border:0" allowfullscreen Distribute content evenly></iframe>
				<p style="font-size: 9px;">Source: Github JHU EDU  </p>

				</div>
			</div>

			<div class="col-md-4">
				<div class="card card-body h-100">
					<h5>Vaccine supplies/Nguồn vaccine</h5>
					<hr>
					<p><div id="piechart"></div>
					</p>
					<p style="font-size: 9px;">Source: "Total Doses Received" - Phanxuandung.notion.site </p>
					<p style="font-size: 9px;">"NANOCOVAX is the Vietnam's homegrown COVID-19 vaccine candidate researched and developed by Nanogen based on recombinant DNA/protein technology. It has not been approved and is under the third-phase clinical trial, which started on June 11, 2021."</p>

					
				</div>
			</div>
		</div>
	</div>
</section>
	<br>
	<section class="s2">
		<div class="description">
			<div class="description-overlay">
				<div class="container">
					<p><h3>The Effective Reproduction Rate (R) and Model </h3>
					</p>
					<hr>
					<p> </p>
				</div>
			</div>
		</div>
	</section>		
	<br>
	<section class="s1">
		<div class="container">
		<div class="row" >
			<div class="col-md-3">
				<div class="card card-body h-100" id="contact">
				<h4>Related Links</h4>
				<p>
				<h6>
				<ul><a href="https://ncov.moh.gov.vn">MOH</a></ul>
				<ul><a href="https://vnexpress.net/covid-19/vaccine">Vnexpress</a></ul>
				<ul><a href="https://coronavirus.jhu.edu/region/vietnam">JHU CSSE</a></ul>
				<ul><a href="https://phanxuandung.notion.site/phanxuandung/Vietnam-s-COVID-19-Vaccine-Situation-T-nh-h-nh-Vaccine-COVID-19-t-i-Vi-t-Nam-60dfadf98dd94f24b89c1f7f69614e9c">PXD NotionSite</a></ul>
				
				

				</h6>
			</p>
				</div>
			</div>

			<div class="col-md-9">
				<div class="card card-body h-100" id="contact" >
					<h5>Contact Me</h5>
					<p><h6>If you have any feedback, question, or request you can contact me via the contact form on this page</h6></p>

					<h6>Past project:
						<ul><a href="https://datastudio.google.com/u/0/reporting/d7f2c5d5-5819-4445-906f-cda8deca38c9/page/0PoLC">Dashboard</a></ul>
						<ul><a href="https://michellehlcn.github.io/covid19hotspot/">Map: HCMC's Covid Hotspot</a>
						</ul>
					</h6>

					<button class="open-button" onclick="openForm()">Open Form</button>

					<div class="form-popup" id="myForm">
  					<form action="mailto:michellehlcn.au@gmail.com" class="form-container">
    				<h1>Login</h1>

   					 <label for="Name"><b>Name</b></label>
   					 <input type="text" placeholder="Enter Name" name="name" required>

    				<label for="feedback"><b>Feedback</b></label>
    				<input type="text" placeholder="Your Feedback" name="feedback" required>

    				<button type="submit" class="btn">Send</button>
    				<button type="button" class="btn cancel" onclick="closeForm()">Close</button>
  					</form>
					</div>

				</div>
			</div>
		</div>

		<br>


	</div>


</section>	

<script type="text/javascript" src="js/mdb.min.js"></script>
<script type="text/javascript">
let xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
	if (this.readyState == 4 && this.status ==200) {
		let data = JSON.parse(this.responseText).feed.entry;


		let i;
		for (i= 0; i< data.length; i++) {
			let state = data[i]["gsx$_cn6ca"]["$t"];
			let new_cases = data[i]["gsx$_cokwr"]["$t"];
			let change = data[i]["gsx$_cpzh4"]["$t"];
			let total = data[i]["gsx$_cre1l"]["$t"];

			
			document.getElementById('demo').innerHTML +=
			"<tr>" +
			"<td>" +
			state +
			"</td>" +
			"<td>" +
			new_cases +
			"</td>" +
			"<td>" +
			change +
			"</td>" +
			"<td>" +
			total +
			"</td>" +
			"</tr>";

		}
	}
};

xmlhttp.open(
	"GET",
	"https://spreadsheets.google.com/feeds/list/1tD1rO9c4SqQZ_KraM6AzWHd1K57uXM6gouvyXBE0jnM/6/public/values?alt=json",
	true 
);

xmlhttp.send();


</script>
<script type="text/javascript">
$(function() {
	$('.table table-striped> tr').clone().appendTo('.table table-striped tbody').addClass('hidden-to-set-col-widths');

  for (var i = 0; i < 20; i++) {
    var a = Math.floor(10 * Math.random());
    var b = Math.floor(10 * Math.random());

    var row = $("<tr>").append($("<td>").html(a + " + " + b + " ="))
      .append($("<td>").html(a + b))
      .append($("<td>").html('blah'))
      .append($("<td>").html('derp'));
    $("tbody").append(row);
  }
});

</script>

 <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Source', 'Doses'],
          ['AstraZeneca_Japan_Donation', 3000000],
          ['AstraZeneca_COVAX_Donation', 3673600],
          ['AstraZeneca_Purchase', 3759900],
          ['AstraZeneca_TheUK_Donation', 415000],
          ['Moderna_TheUS_Donation', 5000000],
          ['Pfizer_Purchase', 194000],
          ['Sputnik V_Russia_Donation', 2000],
          ['Sinopharm_China_Donation', 500000],
          ['Sinopharm_China_Purchase', 1000000],
        ]);

        var options = {
          title: '',
          legend: 'none',
          chartArea:{left:0,top:0,width:"100%"},
        

        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>


    <script>function openForm() {
  document.getElementById("myForm").style.display = "block";
}

			function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
	</script>

</body>
</html>

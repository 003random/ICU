echo "
<html>
<head>
  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">
   <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">
  <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js\"></script>
  <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js\"></script>
</head>
<body>
<div id=\"top-image\" style=\"overflow-y: scroll;\">
<?php
\$servername = \"$3\";
\$username = \"$1\";
\$password = \"$2\";
\$dbname = \"recon\";

\$conn = new mysqli(\$servername, \$username, \$password, \$dbname);

if (\$conn->connect_error) {
    die(\"Connection failed: \" . \$conn->connect_error);
}

\$sql = \"SELECT * FROM domains ORDER BY Active\";

\$result = \$conn->query(\$sql);

if (\$result->num_rows > 0) {
    while(\$row = \$result->fetch_assoc()) {
        \$rows[] = \$row;
   }
} else {
    echo \"0 results\";
}
\$conn->close();

\$domains = array();

        foreach (\$rows as \$r) {
                if(empty(\$r[\"TopDomainID\"])){
                        \$subdomains = array();
                        foreach (\$rows as \$r2) {
                                if(\$r2[\"TopDomainID\"] == \$r[\"DomainID\"]){
                                        array_push(\$subdomains, \$r2);
                                }
                        }
                        array_push(\$domains, array(\$r, \$subdomains));
                }

        }
?>

<ul id=\"accordion\" class=\"accordion\">
        <li>
                <div class=\"link\" style=\"\">
                        <i class=\"fa fa-search\" style=\"margin-top: 5px;\" ></i>
                        <input type=\"text\" class=\"form-control\" id=\"search\">
                </div>
        </li>
        <?php
                foreach (\$domains as &\$domain) {
                        if(\$domain != ''){
                        echo '
                        <li><div class=\"link top-domain\"><i class=\"fa fa-globe\"></i>'.\$domain[0][\"Domain\"].'<i class=\"fa fa-chevron-down\"></i></div>
                                <ul class=\"submenu\">';
                                        \$domain[1] = array_reverse(\$domain[1], true);
                                        foreach (\$domain[1] as \$d) {
                                                echo '<li class=\"subdomain\" added=\"'.\$d[\"LastModified\"].'\" active=\"'.\$d[\"Active\"].'\" inscope=\"'.\$d[\"InScope\"].'\" program=\"'.\$d[\"Program\"].'\"><a href=\"#\">'.\$d[\"Domain\"].'</a></li>';
                                        }
                        echo '</ul></li>';
                        }
                }
        ?>
</ul>

<style>
.modal-backdrop {
top: -5000px !important;
position: static;
}

#top-image {
background:url('http://goldwallpapers.com/uploads/posts/google-data-center-wallpaper/google_data_center_wallpaper_013.jpg') -25px -50px;
position:fixed ;
top:0;
width:100%;
z-index:0;
  height:100%;
  background-size: calc(100% + 50px);
}

* {
        margin: 0;
        padding: 0;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
}

body {
        background: #2d2c41;
        font-family: 'Open Sans', Arial, Helvetica, Sans-serif, Verdana, Tahoma;
}

ul {
        list-style-type: none;
}

a {
        color: #b63b4d;
        text-decoration: none;
}

/** =======================
 * Contenedor Principal
 ===========================*/
h1 {
        color: #FFF;
        font-size: 24px;
        font-weight: 400;
        text-align: center;
        margin-top: 80px;
 }

h1 a {
        color: #c12c42;
        font-size: 16px;
 }

 .accordion {
        width: 100%;
        max-width: 360px;
        margin: 30px auto 20px;
        background: #FFF;
        -webkit-border-radius: 4px;
        -moz-border-radius: 4px;
        border-radius: 4px;
 }

.accordion .link {
        cursor: pointer;
        display: block;
        padding: 15px 15px 15px 42px;
        color: #4D4D4D;
        font-size: 14px;
        font-weight: 700;
        border-bottom: 1px solid #CCC;
        position: relative;
        -webkit-transition: all 0.4s ease;
        -o-transition: all 0.4s ease;
        transition: all 0.4s ease;
}

.accordion li:last-child .link {
        border-bottom: 0;
}

.accordion li i {
        position: absolute;
        top: 16px;
        left: 12px;
        font-size: 18px;
        color: #595959;
        -webkit-transition: all 0.4s ease;
        -o-transition: all 0.4s ease;
        transition: all 0.4s ease;
}

.accordion li i.fa-chevron-down {
        right: 12px;
        left: auto;
        font-size: 16px;
}

.accordion li.open .link {
        color: #b63b4d;
}

.accordion li.open i {
        color: #b63b4d;
}
.accordion li.open i.fa-chevron-down {
        -webkit-transform: rotate(180deg);
        -ms-transform: rotate(180deg);
        -o-transform: rotate(180deg);
        transform: rotate(180deg);
}

.accordion li.default .submenu {display: block;}
/**
 * Submenu
 -----------------------------*/
 .submenu {
        display: none;
        background: #FE8103;
        font-size: 14px;
 }

 .submenu li {
        border-bottom: 1px solid white;
 }

 .submenu a {
        display: block;
        text-decoration: none;
        color: #d9d9d9;
        padding: 12px;
        padding-left: 42px;
        -webkit-transition: all 0.25s ease;
        -o-transition: all 0.25s ease;
        transition: all 0.25s ease;
 }

 .submenu a:hover {
        background: #801B0C;
        color: #FFF;
 }


</style>


<!-- Modal -->
<div id=\"myModal\" class=\"modal fade\" role=\"dialog\">
  <div class=\"modal-dialog\">

    <!-- Modal content-->
    <div class=\"modal-content\">
      <div class=\"modal-header\">
        <button type=\"button\" class=\"close\" data-dismiss=\"modal\">&times;</button>
        <h4 class=\"modal-title\">Info</h4>
      </div>
      <div class=\"modal-body\">
        <p>body text</p>
      </div>
      <div class=\"modal-footer\">
        <button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Close</button>
      </div>
    </div>

  </div>
</div>


<script>
\$(function() {

var movementStrength = 25;
var height = movementStrength / \$(window).height();
var width = movementStrength / \$(window).width();
\$(\"body\").mousemove(function(e){
          var pageX = e.pageX - (\$(window).width() / 2);
          var pageY = e.pageY - (\$(window).height() / 2);
          var newvalueX = width * pageX * -1 - 25;
          var newvalueY = height * pageY * -1 - 50;
          \$('#top-image').css(\"background-position\", newvalueX+\"px     \"+newvalueY+\"px\");
});
\$(\"#search\").keyup(function(){
        \$('.top-domain').each(function(i, obj) {
                if(\$(this).text().indexOf(\$(\"#search\").val()) == -1){
                        \$(this).hide();
                }else{
                        \$(this).show();
                }
        });
});


\$(\".subdomain\").on('click',function(){
        \$(\".modal-body\").text(\"\");
        \$(\".modal-body\").append(\"Domain: <b>\"+\$(this).children().text()+\"</b>\");
        \$(\".modal-body\").append(\"</br>\");
        \$(\".modal-body\").append(\"Last Modified: <b>\"+\$(this).attr(\"added\")+\"</b>\");
        \$(\".modal-body\").append(\"</br>\");
        \$(\".modal-body\").append(\"Active: <b>\"+\$(this).attr(\"active\").replace(\"1\", \"Yes\").replace(\"0\", \"No\")+\"</b>\");
        \$(\".modal-body\").append(\"</br>\");
        \$(\".modal-body\").append(\"Inscope: <b>\"+\$(this).attr(\"inscope\").replace(\"1\", \"Yes\").replace(\"0\", \"No\")+\"</b>\");
        \$(\".modal-body\").append(\"</br>\");
        \$(\".modal-body\").append(\"Program: <b>\"+\$(this).attr(\"program\")+\"</b>\");


        \$('#myModal').modal('show');
});

        var Accordion = function(el, multiple) {
                this.el = el || {};
                this.multiple = multiple || false;

                // Variables privadas
                var links = this.el.find('.link');
                // Evento
                links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
        }

        Accordion.prototype.dropdown = function(e) {
                var \$el = e.data.el;
                        \$this = \$(this),
                        \$next = \$this.next();

                \$next.slideToggle();
                \$this.parent().toggleClass('open');

                if (!e.data.multiple) {
                        \$el.find('.submenu').not(\$next).slideUp().parent().removeClass('open');
                };
        }

        var accordion = new Accordion(\$('#accordion'), false);
});
</script>
</div>
</body>

" > /var/www/html/ICU.php

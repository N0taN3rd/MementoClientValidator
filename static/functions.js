function addHeaderTags() {
    var spans = document.getElementsByTagName("span");
    for (var i = 0; i < spans.length; i++) {
        var elem = spans[i];
        if (elem) {
            var level = elem.getAttribute("class");
            if (level == "h1" || level == "h2" || level == "h3" || level == "h4" || level == "h5" || level == "h6") {
                elem.innerHTML = "<" + level + ">" + elem.innerHTML + "</" + level + ">";
            }
        }
    }
}
var legend_html = "Colour legend:<br />      <table>         <tr><td>Unknown:</td>                   <td><span class='cplate bgwhite'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Draft:</td>                     <td><span class='cplate bgred'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Informational:</td>             <td><span class='cplate bgorange'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Experimental:</td>              <td><span class='cplate bgyellow'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Best Common Practice:</td>      <td><span class='cplate bgmagenta'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Proposed Standard:</td>         <td><span class='cplate bgblue'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Draft Standard (old designation):</td> <td><span class='cplate bgcyan'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Internet Standard:</td>         <td><span class='cplate bggreen'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Historic:</td>                  <td><span class='cplate bggrey'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Obsolete:</td>                  <td><span class='cplate bgbrown'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>     </table>";
function showElem(id) {
    var elem = document.getElementById(id);
    elem.innerHTML = eval(id + "_html");
    elem.style.visibility = 'visible';
}
function hideElem(id) {
    var elem = document.getElementById(id);
    elem.style.visibility = 'hidden';
    elem.innerHTML = "";
}
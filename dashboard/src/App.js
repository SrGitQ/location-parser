import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import { ComposableMap, Geographies, Geography } from "react-simple-maps"

const geoUrl = "https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries.json"

const MapChart = () => {
  return (
    <ComposableMap>
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography key={geo.rsmKey} geography={geo} />
          ))
        }
      </Geographies>
    </ComposableMap>
  )
}

const App = () => {
  const printDocument = () => {
    const input = document.getElementById('divToPrint');
    html2canvas(input)
      .then((canvas) => {
        const imgData = canvas.toDataURL('image/png');
        const pdf = new jsPDF();
        pdf.addImage(imgData, 'JPEG', 0, 0);
        // pdf.output('dataurlnewwindow');
        pdf.save("dashboard.pdf");
      })
    ;
  }//<iframe width="560" height="315" src="https://www.youtube.com/embed/wKRL7vkWMoc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  return (
    <div>
      <div id='divToPrint'>
        <h1>Dashboard</h1>
        <p>Some content</p>
        <div style={{width:'500px'}}>
          <MapChart/>
        </div>
        
      </div>
      <button  onClick={printDocument}>Download PDF</button>
    </div>
  );
}

export default App;

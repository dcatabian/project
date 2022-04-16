var NewComponent = React.createClass({
    render: function() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <link rel="stylesheet" href="style.css" />
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossOrigin="anonymous" />
          <title>Member Information</title>
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
            </div>
          </nav>
          <section className="container">
            <div className="card">
              <div className="card-image pr-pic" />
              <h2><center>Submit Purchase Request</center></h2>
              <a href="submitrequestForm.html">Click Here</a>
            </div>
            <div className="card">
              <div className="card-image id-pic" />
              <h2><center>View Inventory Database</center></h2>
              <a href="memInventoryView.html">Click Here</a>
            </div>
            <div className="card">
              <div className="card-image sr-pic" />
              <h2><center>Submitted Requests</center></h2>
              <a href="memSubmitRequest.html">Click Here</a>
            </div>
          </section>
          <style dangerouslySetInnerHTML={{__html: "\n        body{\n            background: #68686b;\n           \n        }\n    " }} />
        </div>
      );
    }
  });
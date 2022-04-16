var NewComponent = React.createClass({
    render: function() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Document</title>
          <style dangerouslySetInnerHTML={{__html: "\n        * {\n        \n        font-family: sans-serif; /* Change your font family */\n    }\n\n    .content-table {\n    border-collapse: collapse;\n    /* margin: 25px 0; */\n    margin-left: auto;\n    margin-right: auto;\n    text-align: center;\n\n    font-size: 0.9em;\n    min-width: 400px;\n    border-radius: 5px 5px 0 0; \n    overflow: hidden;\n    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);\n    }\n\n    .content-table thead tr {\n    background-color: #009879;\n    color: #ffffff;\n    text-align: left;\n    font-weight: bold;\n    }\n\n    .content-table th,\n    .content-table td {\n    padding: 12px 15px;\n    }\n\n    .content-table tbody tr {\n    border-bottom: 1px solid #dddddd;\n    }\n\n    .content-table tbody tr:nth-of-type(even) {\n    background-color: #f3f3f3;\n    }\n\n    .content-table tbody tr:last-of-type {\n    border-bottom: 2px solid #009879;\n    }\n\n    .content-table tbody tr.active-row {\n    font-weight: bold;\n    color: #009879;\n    }\n        " }} />
          <table className="content-table">
            <thead>
              <tr>
                <th>Item Name</th>
                <th>Quantity</th>
                <th>Possessed</th>
                <th>Possessed By</th>
                <th>Invoice ID</th> 
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Chair</td>
                <td>10</td>
                <td>Yes</td>
                <td>Derrick</td>
                <td>1</td>
              </tr>
              <tr className="active-row">
                <td>Table</td>
                <td>12</td>
                <td>No</td>
                <td>Godwin</td>
                <td>2</td>
              </tr>
              <tr>
                <td>Computer</td>
                <td>4</td>
                <td>N/A</td>
                <td>N/A</td>
                <td>3</td>
              </tr>
              <tr>
                <td>Washing Machine</td>
                <td>2</td>
                <td>N/A</td>
                <td>N/A</td>
                <td>1</td>
              </tr>
            </tbody>
          </table>
        </div>
      );
    }
  });
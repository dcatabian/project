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
                <th>ID</th>
                <th>Item</th>
                <th>Date of Approval</th>
                {/* What shall be under original purchase request? */}
                <th>Original Purchase Request</th>
                <th>Fullfilment Status</th>
                <th>Fullfilment Date</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>26-7-22</td>
                <td>Approved</td>
                <td>26-7-22</td>
              </tr>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>Linked Request</td>
                <td>In Progress</td>
                <td>N/A</td>
              </tr>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>Linked Request</td>
                <td>Purchased</td>
                <td>26-7-22</td>
              </tr>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>26-7-22</td>
                <td>Approved</td>
                <td>26-7-22</td>
              </tr>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>26-7-22</td>
                <td>Approved</td>
                <td>26-7-22</td>
              </tr>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>26-7-22</td>
                <td>Approved</td>
                <td>26-7-22</td>
              </tr>
              <tr>
                <td>1234567</td>
                <td>Chair</td>
                <td>23-7-22</td>
                <td>26-7-22</td>
                <td>Approved</td>
                <td>26-7-22</td>
              </tr>
            </tbody>
          </table>
        </div>
      );
    }
  });
var NewComponent = React.createClass({
    render: function() {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <link rel="stylesheet" href="style.css" />
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossOrigin="anonymous" />
          {/* Hello there */}
          <title>Treasury Login Page</title>
          {/* Member Login Form  */}
          <div className="text-center mt-5">
            <form action="Treasury.html" style={{maxWidth: '480px', margin: 'auto'}} post">
              <img src alt="" />
              <h1 className="h3 mb-3 font-weight-normal">Treasury Login</h1>
              <label htmlFor="email_address" className="sr-only" />
              <input type="email" id="email_address" className="form-control" placeholder="Enter your email here." required autofocus />
              <label htmlFor="password" className="sr-only" />
              <input type="password" id="password" placeholder="Enter your password here." className="form-control" />
              <br />
              <button className="btn btn-lg btn-primary btn-block" onclick>Sign In</button>
            </form></div>
          <style dangerouslySetInnerHTML={{__html: "\n        body{\n            background: #f09053;\n            color:#383a58;\n        }\n    " }} />
        </div>
      );
    }
  });
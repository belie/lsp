# lsp
the web interface to the LSP project
<pre>
Main Display URL
This will show the results of the QA and Production Docker builds
<site>/results

QA Status URL
<site>/qa_status
This will provide an updated status for the qa jenkins run.
Returns
{last_updated: "2012-01-04" 12:15:00", status: "Success"}

Deployment Status URL
<site>/deploy_status
This will provide an updated status for the production deployment
{last_updated: "2012-01-04" 12:15:00", status: "Success"}
</pre>

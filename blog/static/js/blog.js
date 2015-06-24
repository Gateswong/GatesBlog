function verifyBlogBody() {
  var firstLine = $("#blog-body-input").val();

  if (firstLine && firstLine.split("\n")[0].trim().match(/^\[\[\s*\w+\s*\]\]$/)) {
    return true;
  }
  console.log("verifyBlogBody: failed");
  $("#blog-body-helper").modal("toggle");
  return false;
};




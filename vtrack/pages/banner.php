<?php 
$product_name = wc_get_product()->get_name();
$store_url = get_bloginfo( 'url' );
?>
<style>
.banner {
    background-color: red;
    padding: 10px;
    color: white;
}
</style>
<div class="banner">56 others viewed this recently </div>
<script>
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var raw = JSON.stringify({
    "product_name": '<?php echo $product_name ?>',
    "store_url": '<?php echo $store_url ?>',
});

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

fetch("<?php echo apiUrl(); ?>api/add-hit", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
</script>
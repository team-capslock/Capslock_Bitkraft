<?php  
    $args = array(
        'orderby'  => 'name',
    );
    $hi = "om";
    $products = wc_get_products( $args );
    $arrLength = count($products);
    
    $new_products = array(array());
    
    for($i = 0; $i < $arrLength; $i++) {
        $new_products[$i][0] =  $products[$i]->name;
        $new_products[$i][1] = $products[$i]->description;
        $new_products[$i][2] = $products[$i]->price;
        // $product_obj = new WC_Product( $products[$i]->id );
        // $new_products[$i][3] = $product_obj->get_image();
        $image_id  = $products[$i]->get_image_id();
        $new_products[$i][3] = wp_get_attachment_image_url( $image_id, 'full' );
        
    }
    $out = implode("&",array_map(function($a) {return implode("~",$a);},$new_products));
    $json = json_encode($new_products);
    $store_url = get_bloginfo( 'url' );    
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Goto</title>
</head>

<body>
    <div
        class="flex items-center justify-center min-h-screen from-[#ffffff] via-[#ffffff] to-[#ffffff] bg-gradient-to-br px-2">
        <div class="w-full max-w-md mx-auto bg-white rounded-3xl shadow-xl overflow-hidden">
            <div class="max-w-md mx-auto">
                <div class="h-[236px]" style="
                background-image: url(data:image/png;base64,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);
                background-position: center;
                background-repeat: no-repeat;
              "></div>
                <div class="p-4 sm:p-6">
                    <button onclick="sync()"
                        class="block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#000000] rounded-[14px] hover:bg-[#252525dd] focus:outline-none focus:ring text-white focus:ring-teal-300 focus:ring-opacity-80">
                        Visit Dashboard
                    </button>

                    <p class="text-[#7C7C80] font-[15px] mt-6">
                        Get all reports and updates.
                    </p>
                </div>
            </div>
        </div>
    </div>

</body>

</html>
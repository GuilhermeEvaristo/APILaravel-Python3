<?php

namespace App\Http\Controllers\Api;
use App\Produto;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\API\ApiError;
class ProductController extends Controller
{
    public function __construct(Produto $product){

        $this->produto = $product;
    }

    public function index(){
        $data = ['data' => $this->produto->get()];
        return response()->json($data);
    }
    public function store(Request $request){
        try{
            $this->produto->create([
                'name'=>$request->name,
            ]);
            return response()->json(['msg'=>"Deu Certo!"], 201);
        }catch(\Exception $e){
            if(config('app.debug')){
                return response()->json(ApiError::errorMessage($e->getMessage(), 1010));
            }
            return response()->json(ApiError::errorMessage("tem um erro ai.", 1010));
        }
    }
}

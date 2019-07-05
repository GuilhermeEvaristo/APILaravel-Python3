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

        $data = ['data' => $this->produto->with('categorias')->get()];
        return response()->json($data);
    }
    public function show(Produto $id){
        $data = ['id'=> $id];
        return response()->json($data);
    }
    public function store(Request $request){
        try{
            $this->produto->create([
                'name'=>$request->name,
                'description'=>$request->description,
                'categoria_id'=>$request->categoria_id,
            ]);
            return response()->json(['msg'=>"Deu Certo!"], 201);
        }catch(\Exception $e){
            if(config('app.debug')){
                return response()->json(ApiError::errorMessage($e->getMessage(), 1010));
            }
            return response()->json(ApiError::errorMessage("tem um erro ai.", 1010));
        }
    }
    public function update(Request $request, $id){
        $productData = $request->all();
        $product = $this->produto->find($id);
        $product->update($productData);
        try{
            $this->produto->create($productData);
            return response()->json(['msg'=>"Atualizado com Sucesso!"], 200);
        }catch(\Exception $e){
            if(config('app.debug')){
                return response()->json(ApiError::errorMessage($e->getMessage(), 1010));
            }
            return response()->json(ApiError::errorMessage("tem um erro ai.", 1010));
        }
    }
    public function delete($id){
        $product = $this->produto->find($id);
        $product->delete();
    }
    public function deleteAll(){
        $product = $this->produto->get();
        foreach($product as $item){
            $teste = $product->find($item['id']);
            $teste->delete();
        }
        // $product->delete();
    }
}

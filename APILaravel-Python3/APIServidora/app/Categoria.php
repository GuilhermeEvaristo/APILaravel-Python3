<?php

namespace App;
use App\Produto;
use Illuminate\Database\Eloquent\Model;

class Categoria extends Model
{
    protected $fillable  = [
        'name'
    ];
    function produtos(){
        return $this->hasMany('App\Produto');
    }
}

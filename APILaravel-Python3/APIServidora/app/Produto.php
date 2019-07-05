<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Produto extends Model
{
    protected $fillable  = [
        'name', 'categoria_id', 'description'
    ];
    function categorias(){
        return $this->belongsTo('App\Categoria', 'categoria_id', 'id');
    }
}

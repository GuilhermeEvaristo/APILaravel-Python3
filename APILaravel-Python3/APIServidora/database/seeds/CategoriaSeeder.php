<?php

use Illuminate\Database\Seeder;
use App\Categoria;
class CategoriaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Categoria::create(['name'=>'Gospel']);
        Categoria::create(['name'=>'Sertanejo']);
        Categoria::create(['name'=>'Funk']);
    }
}

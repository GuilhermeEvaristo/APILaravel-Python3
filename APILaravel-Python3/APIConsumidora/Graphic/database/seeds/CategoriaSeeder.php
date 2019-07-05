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
        Categoria::create(['name'=>'Comédia']);
        Categoria::create(['name'=>'Terror']);
        Categoria::create(['name'=>'Super herói']);
    }
}

import Hero from "./components/Hero";
// Importaremos los otros cuando los crees:
import Navbar from "./components/Navbar";
import ProductGrid from "./components/ProductGrid";



function App() {
  return (
   <div className="min-h-screen bg-gray-50">
  <Navbar /> {/* <-- Sin las llaves se ve mejor */}
  <main>
    <Hero />
    <ProductGrid /> {/* <-- Aquí también quítale las llaves */}
  </main> 
  <footer className="py-6 text-center text-gray-500">
    © 2026 EcuaTrade - Desde Babahoyo para el mundo
  </footer>
</div>
  );
}

export default App;
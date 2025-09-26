"""
Spacetime Dilation Simulator

This module implements the core spacetime dilation calculations
comparing different gravitational environments:
- Cosmonauts near black hole event horizons
- Earth-based observers
- Quantum particle reference frames
"""

import numpy as np
import matplotlib.pyplot as plt


class SpacetimeDilationSimulator:
    """Simulates time dilation effects between different reference frames"""
    
    def __init__(self):
        # Physical constants (natural units: c=1, G=1)
        self.c = 1.0  # Speed of light
        self.G = 1.0  # Gravitational constant
        
        # Masses (in natural units)
        self.M_earth = 1.0  # Earth mass (reference)
        self.M_black_hole = 1000.0  # Stellar black hole mass
        
    def schwarzschild_time_dilation(self, mass, radius):
        """
        Calculate time dilation factor using Schwarzschild metric
        
        Args:
            mass: Gravitational mass
            radius: Distance from mass center
            
        Returns:
            Time dilation factor (proper time / coordinate time)
        """
        schwarzschild_radius = 2 * self.G * mass / (self.c ** 2)
        
        if radius <= schwarzschild_radius:
            return 0.0  # At or inside event horizon
            
        return np.sqrt(1 - schwarzschild_radius / radius)
    
    def simulate_cosmonaut_vs_earth(self, cosmonaut_distance_factor=1.1):
        """
        Simulate time dilation between cosmonaut near black hole
        and home office worker on Earth
        
        Args:
            cosmonaut_distance_factor: How close to event horizon (1.0 = exactly at horizon)
        """
        # Cosmonaut position (just outside event horizon)
        r_schwarzschild = 2 * self.G * self.M_black_hole / (self.c ** 2)
        r_cosmonaut = cosmonaut_distance_factor * r_schwarzschild
        
        # Earth observer position (Earth surface)
        r_earth = 6371  # km in natural units
        
        # Calculate time dilation factors
        tau_cosmonaut = self.schwarzschild_time_dilation(self.M_black_hole, r_cosmonaut)
        tau_earth = self.schwarzschild_time_dilation(self.M_earth, r_earth)
        
        # Relative time dilation
        relative_dilation = tau_earth / tau_cosmonaut if tau_cosmonaut > 0 else float('inf')
        
        return {
            'cosmonaut_dilation': tau_cosmonaut,
            'earth_dilation': tau_earth,
            'relative_dilation': relative_dilation,
            'cosmonaut_distance': r_cosmonaut,
            'schwarzschild_radius': r_schwarzschild
        }
    
    def quantum_scale_analogy(self, quantum_curvature_factor=1e6):
        """
        Apply the same dilation principles to quantum scales
        
        Args:
            quantum_curvature_factor: Hypothetical spacetime curvature at quantum scales
        """
        # Hypothetical quantum "mass" creating extreme local curvature
        m_quantum_effective = quantum_curvature_factor * self.M_earth
        r_quantum = 1e-15  # Roughly nuclear scale
        
        # Calculate quantum-scale time dilation
        tau_quantum = self.schwarzschild_time_dilation(m_quantum_effective, r_quantum)
        tau_macro = self.schwarzschild_time_dilation(self.M_earth, 6371)
        
        quantum_relative_dilation = tau_macro / tau_quantum if tau_quantum > 0 else float('inf')
        
        return {
            'quantum_dilation': tau_quantum,
            'macro_dilation': tau_macro,
            'quantum_relative_dilation': quantum_relative_dilation,
            'effective_quantum_mass': m_quantum_effective
        }
    
    def plot_dilation_comparison(self):
        """Create visualization comparing different dilation scenarios"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Plot 1: Cosmonaut vs Earth observer
        distances = np.linspace(1.01, 10, 100)  # Distance factors from event horizon
        dilations = []
        
        for d in distances:
            result = self.simulate_cosmonaut_vs_earth(d)
            dilations.append(result['relative_dilation'])
        
        ax1.plot(distances, dilations)
        ax1.set_xlabel('Distance from Event Horizon (Schwarzschild radii)')
        ax1.set_ylabel('Time Dilation Factor (Earth/Cosmonaut)')
        ax1.set_title('Cosmonaut vs Earth Observer Time Dilation')
        ax1.set_yscale('log')
        ax1.grid(True)
        
        # Plot 2: Quantum scale analogy
        curvature_factors = np.logspace(3, 8, 100)
        quantum_dilations = []
        
        for cf in curvature_factors:
            result = self.quantum_scale_analogy(cf)
            quantum_dilations.append(result['quantum_relative_dilation'])
        
        ax2.plot(curvature_factors, quantum_dilations)
        ax2.set_xlabel('Quantum Curvature Factor')
        ax2.set_ylabel('Time Dilation Factor (Macro/Quantum)')
        ax2.set_title('Quantum Scale Time Dilation Analogy')
        ax2.set_xscale('log')
        ax2.set_yscale('log')
        ax2.grid(True)
        
        plt.tight_layout()
        return fig


if __name__ == "__main__":
    # Example usage
    simulator = SpacetimeDilationSimulator()
    
    # Simulate cosmonaut scenario
    cosmonaut_result = simulator.simulate_cosmonaut_vs_earth(1.1)
    print("Cosmonaut vs Earth Simulation:")
    print(f"  Cosmonaut time dilation: {cosmonaut_result['cosmonaut_dilation']:.6f}")
    print(f"  Earth time dilation: {cosmonaut_result['earth_dilation']:.6f}")
    print(f"  Relative dilation: {cosmonaut_result['relative_dilation']:.2f}x")
    
    # Simulate quantum analogy
    quantum_result = simulator.quantum_scale_analogy(1e6)
    print("\nQuantum Scale Analogy:")
    print(f"  Quantum time dilation: {quantum_result['quantum_dilation']:.10f}")
    print(f"  Macro time dilation: {quantum_result['macro_dilation']:.6f}")
    print(f"  Quantum relative dilation: {quantum_result['quantum_relative_dilation']:.2e}x")
    
    # Create visualization
    fig = simulator.plot_dilation_comparison()
    plt.show()